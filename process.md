1) make a db in psql and add pgvector extension:
CREATE EXTENSION vector;

-- Verify it worked (should print a version number)
SELECT * FROM pg_available_extensions WHERE name = 'vector';

2) intall below libraries:
pip install crewai crewai-tools langchain_postgres psycopg2-binary pandas openpyxl duckduckgo-search

3) create a test file that will check all the moving parts individually

4) create a db manager and its testing file

5) create the dsa loader and its testing file

6) create a directory for agents and store each agent over there
 -> researcher.py
 -> architecture.py
 -> integration tester for above both : test_integration_ra.py
 -> engineer.py
 -> integration tester for above three : test_integration_rae.py
 -> professor.py
 