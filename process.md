1) make a db in psql and add pgvector extension:
CREATE EXTENSION vector;

-- Verify it worked (should print a version number)
SELECT * FROM pg_available_extensions WHERE name = 'vector';

2) intall below libraries:
pip install crewai crewai-tools langchain_postgres psycopg2-binary pandas openpyxl duckduckgo-search

3) create a test file that will check all the moving parts individually
