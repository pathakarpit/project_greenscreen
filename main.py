import os
import re
from crewai import Crew, Process
from dotenv import load_dotenv

# --- LOCAL MODULE IMPORTS ---
from db_manager import DBManager
from dsa_loader import DSALoader
from agents.researcher import get_researcher_agent, get_research_task
from agents.architect import get_architect_agent, get_architect_task
from agents.engineer import get_engineer_agent, get_coding_task
from agents.professor import get_professor_agent, get_analysis_task

# Load environment variables
load_dotenv()

# --- CONFIGURATION ---
EXCEL_PATH = os.getenv("INPUT_EXCEL_PATH", "data/input/questions.xlsx")
SHEET_NAME = os.getenv("SHEET_NAME", "main_questions")
QUESTION_FILE = "question.txt"
SOLUTION_FILE = "solution.py"

def save_to_files(target, problem_text, solution_code, explanation):
    """
    Saves the agent outputs to files for the Git commit.
    Includes robust sanitization to strip LLM chatter and Markdown.
    """
    
    # --- 1. CLEAN THE PYTHON CODE ---
    raw_code = str(solution_code)
    
    # Remove Markdown backticks (common LLM habit)
    clean_code = raw_code.replace("```python", "").replace("```", "").strip()
    
    # Remove conversational filler before the class definition
    # This finds where "class Solution" starts and discards everything before it.
    if "class Solution" in clean_code:
        start_index = clean_code.find("class Solution")
        clean_code = clean_code[start_index:]
    else:
        # Fallback if strict mode failed completely (rare), just comment it out
        clean_code = f"# WARNING: Valid Class Definition Not Found\n# Raw Output:\n{clean_code}"

    # --- 2. WRITE SOLUTION.PY ---
    with open(SOLUTION_FILE, "w", encoding="utf-8") as f:
        f.write(f"# Problem: {target['title']}\n")
        f.write(f"# Difficulty: {target['difficulty']}\n")
        f.write(f"# Link: {target['link']}\n\n")
        f.write(clean_code)
        
        # Add a dummy main block so the file is runnable (optional but good for testing)
        f.write("\n\n" + "#" * 40)
        f.write("\n# if __name__ == '__main__':\n#     s = Solution()\n#     # print(s.solve(inputs...))")
    
    # --- 3. WRITE QUESTION.TXT ---
    with open(QUESTION_FILE, "w", encoding="utf-8") as f:
        f.write(f"TITLE: {target['title']}\n")
        f.write(f"DIFFICULTY: {target['difficulty']}\n")
        f.write(f"LINK: {target['link']}\n")
        f.write("-" * 40 + "\n\n")
        
        f.write("--- PROBLEM STATEMENT ---\n")
        f.write(str(problem_text).strip() + "\n\n")
        
        f.write("-" * 40 + "\n\n")
        f.write("--- PROFESSOR'S EXPLANATION ---\n")
        f.write(str(explanation).strip() + "\n")

    print(f"\n✅ Files Generated Successfully:\n   - {QUESTION_FILE}\n   - {SOLUTION_FILE}")

def main():
    print("\n🟢 PROJECT GREENSCREEN: DAILY WORKFLOW STARTED")
    print("==============================================")
    
    # --- STEP 1: LOAD DATABASE & QUESTION ---
    try:
        db = DBManager()
        loader = DSALoader(EXCEL_PATH, SHEET_NAME)
    except Exception as e:
        print(f"❌ Critical Init Failed: {e}")
        return

    # Get list of already solved questions
    completed_titles = db.get_completed_titles()
    
    # Pick a new question
    target = loader.get_new_question(completed_titles)
    
    if not target:
        print("🎉 All questions in Excel completed! Resetting Cycle...")
        # Optional: Clear DB history or notify user. For now, we pick a random one.
        target = loader.get_new_question([]) 
    
    print(f"\n🎯 TARGET LOCKED: {target['title']} ({target['difficulty']})")
    print(f"🔗 Link: {target['link']}")

    # --- STEP 2: INITIALIZE AGENTS ---
    print("\n🤖 Waking up the AI Team...")
    researcher = get_researcher_agent()
    architect = get_architect_agent()
    engineer = get_engineer_agent()
    professor = get_professor_agent()

    # --- STEP 3: DEFINE TASKS (WITH CONTEXT LINKS) ---
    print("📋 Assigning Tasks...")
    
    # Task 1: Scrape
    t1_scrape = get_research_task(researcher, target)
    
    # Task 2: Format
    # Explicit instruction to look at Task 1's output
    t2_format = get_architect_task(architect, raw_text="Analyze the raw content provided by the Tech Researcher above.")
    
    # Task 3: Code
    # Explicit instruction to look at Task 2's output
    t3_code = get_coding_task(engineer, problem_description="Use the clean Problem Statement provided by the Problem Architect above.")
    
    # Task 4: Explain
    # Explicit instruction to look at Task 3's output
    t4_explain = get_analysis_task(professor, code_solution="Analyze the Python code provided by the Senior Python Engineer above.")

    # --- STEP 4: EXECUTE PIPELINE ---
    print("\n🚀 Launching Crew (This will take 1-3 minutes)...")
    crew = Crew(
        agents=[researcher, architect, engineer, professor],
        tasks=[t1_scrape, t2_format, t3_code, t4_explain],
        process=Process.sequential,
        verbose=True
    )

    # Run the chain
    result = crew.kickoff()

    # --- STEP 5: SAVE RESULTS ---
    print("\n💾 Saving Data...")
    
    # Extract raw outputs from tasks
    final_prob = t2_format.output.raw
    final_code = t3_code.output.raw
    final_expl = t4_explain.output.raw

    # 1. Save to local files (for Git)
    save_to_files(target, final_prob, final_code, final_expl)

    # 2. Save to Database (for History)
    payload = {
        "title": target['title'],
        "topic": target.get('topic', 'Algorithms'), # Fallback if topic missing
        "difficulty": target['difficulty'],
        "link": target['link'],
        "json_content": {
            "problem_statement": final_prob,
            "solution_code": final_code,
            "explanation": final_expl
        }
    }
    db.save_question(payload)
    db.close()
    
    print("\n🏁 DAILY WORKFLOW COMPLETE.")

if __name__ == "__main__":
    main()