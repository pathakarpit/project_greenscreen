import psycopg2
from psycopg2.extras import execute_values
import ollama
import json
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class DBManager:
    def __init__(self):
        # Fetch configs from .env
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
            response = ollama.embeddings(model=self.embedding_model, prompt=text)
            return response['embedding']
        except Exception as e:
            print(f"Error generating embedding: {e}")
            return []
    
    def get_completed_titles(self):
        self.cursor.execute("SELECT title FROM dsa_questions;")
        return [row[0] for row in self.cursor.fetchall()]
    
    def reset_db(self):
        self.cursor.execute("TRUNCATE TABLE dsa_questions RESTART IDENTITY;")
        self.conn.commit()
        print("⚠ DATABASE RESET: All previous questions cleared.")

    def save_question(self, data):
        print(f"Saving '{data['title']}' to Database...")
        emb = self.get_embedding(data['title'] + " " + data['topic'])
        
        query = """
            INSERT INTO dsa_questions (title, topic, difficulty, link, full_json, embedding)
            VALUES (%s, %s, %s, %s, %s, %s)
            ON CONFLICT (title) DO NOTHING;
        """
        
        # Use data.get('difficulty', 'Medium') to be safe
        difficulty = data.get('difficulty', 'Medium')

        self.cursor.execute(query, (
            data['title'], 
            data['topic'], 
            difficulty,  # <--- DYNAMIC VALUE
            data['link'], 
            json.dumps(data['json_content']), 
            emb
        ))
        self.conn.commit()
        print(f"✅ Successfully archived: {data['title']} ({difficulty})")
    
    def close(self):
        if self.cursor: self.cursor.close()
        if self.conn: self.conn.close()