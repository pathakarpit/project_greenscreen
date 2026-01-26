import psycopg2
import ollama
import json
import os
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()

class DBManager:
    def __init__(self):
        self.params = {
            "dbname": os.getenv("DB_NAME", "dsa_db"),
            "user": os.getenv("DB_USER", "postgres"),
            "password": os.getenv("DB_PASSWORD"),
            "host": os.getenv("DB_HOST", "localhost"),
            "port": os.getenv("DB_PORT", "5432")
        }
        self.embedding_model = os.getenv("MODEL_EMBEDDING", "llama3.1")
        
        try:
            self.conn = psycopg2.connect(**self.params)
            self.cursor = self.conn.cursor()
            self._init_tables()
        except Exception as e:
            print(f"❌ DATABASE CONNECTION FAILED: {e}")
            raise e
        
    def _init_tables(self):
        # Enable vector extension if not exists
        self.cursor.execute("CREATE EXTENSION IF NOT EXISTS vector;")
        
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS dsa_questions (
                id SERIAL PRIMARY KEY,
                title TEXT UNIQUE,
                topic TEXT,
                difficulty TEXT,
                link TEXT,
                full_json JSONB,
                embedding vector(4096), 
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)
        self.conn.commit()

    def get_embedding(self, text):
        try:
            # Using your existing Ollama setup
            response = ollama.embeddings(model=self.embedding_model, prompt=text)
            return response['embedding']
        except Exception as e:
            print(f"Error generating embedding: {e}")
            return []

    def is_duplicate(self, new_title, lookback_days=30, threshold=0.85):
        """
        Checks if a semantically similar question was solved recently.
        Returns: (True/False, Reason string)
        """
        if not new_title: return False, "Empty title"

        # 1. Get embedding for the candidate question
        query_vec = self.get_embedding(new_title)
        if not query_vec:
            return False, "Could not generate embedding"

        # 2. Vector Search in Postgres
        # We find the nearest neighbor in terms of cosine similarity (1 - cosine distance)
        # filtered by the lookback window.
        query = """
            SELECT title, created_at, 1 - (embedding <=> %s::vector) as similarity
            FROM dsa_questions
            WHERE created_at > NOW() - INTERVAL '%s days'
            ORDER BY embedding <=> %s::vector
            LIMIT 1;
        """
        
        self.cursor.execute(query, (query_vec, lookback_days, query_vec))
        result = self.cursor.fetchone()

        if result:
            stored_title, solved_at, similarity = result
            
            if similarity > threshold:
                days_ago = (datetime.now() - solved_at).days
                return True, f"Skipped: Similar to '{stored_title}' (Sim: {similarity:.2f}) solved {days_ago} days ago."
        
        return False, "Unique enough"

    def get_completed_titles(self):
        self.cursor.execute("SELECT title FROM dsa_questions;")
        return [row[0] for row in self.cursor.fetchall()]

    def save_question(self, data):
        print(f"Saving '{data['title']}' to Database...")
        # Embed Title + Topic for better context
        emb = self.get_embedding(data['title'] + " " + data['topic'])
        
        query = """
            INSERT INTO dsa_questions (title, topic, difficulty, link, full_json, embedding)
            VALUES (%s, %s, %s, %s, %s, %s)
            ON CONFLICT (title) DO NOTHING;
        """
        
        difficulty = data.get('difficulty', 'Medium')

        self.cursor.execute(query, (
            data['title'], 
            data['topic'], 
            difficulty, 
            data['link'], 
            json.dumps(data['json_content']), 
            emb
        ))
        self.conn.commit()
        print(f"✅ Successfully archived: {data['title']} ({difficulty})")
    
    def close(self):
        if self.cursor: self.cursor.close()
        if self.conn: self.conn.close()