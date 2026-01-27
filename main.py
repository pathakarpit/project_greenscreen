import os
import json
from crewai import Crew, Process
from dotenv import load_dotenv

# --- LOCAL MODULE IMPORTS ---
from db_manager import DBManager
from dsa_loader import DSALoader
from agents.researcher import get_researcher_agent, get_research_task
from agents.architect import get_architect_agent, get_architect_task
from agents.engineer import get_engineer_agent, get_coding_task
from agents.professor import get_professor_agent, get_analysis_task

load_dotenv()

# --- CONFIGURATION ---
EXCEL_PATH = os.getenv("INPUT_EXCEL_PATH", "data/input/questions.xlsx")
SHEET_NAME = os.getenv("SHEET_NAME", "main_questions")

# Updated File Names
QUESTION_FILE = "question.md"
SOLUTION_FILE = "solution.py"
EXPLANATION_FILE = "explanation.md"
AGENT_LOGS_FILE = "agent_logs.json"

def save_agent_logs(tasks):
    """
    Saves a clean, structured JSON log of what each agent did.
    """
    logs = []
    for task in tasks:
        # CrewAI Task objects store their output in task.output.raw
        logs.append({
            "agent": task.agent.role,
            "task_name": task.description.strip().split('\n')[0], # Grab first line as title
            "full_prompt": task.description,
            "response": task.output.raw
        })
    
    with open(AGENT_LOGS_FILE, "w", encoding="utf-8") as f:
        json.dump(logs, f, indent=2)
    print(f"✅ Agent Logs Saved: {AGENT_LOGS_FILE}")

def save_to_files(target, problem_text, solution_code, explanation):
    # --- 1. CLEAN THE PYTHON CODE ---
    raw_code = str(solution_code)
    clean_code = raw_code.replace("```python", "").replace("```", "").strip()
    
    if "class Solution" in clean_code:
        start_index = clean_code.find("class Solution")
        clean_code = clean_code[start_index:]
    else:
        clean_code = f"# WARNING: Valid Class Definition Not Found\n# Raw Output:\n{clean_code}"

    # --- 2. WRITE SOLUTION.PY ---
    with open(SOLUTION_FILE, "w", encoding="utf-8") as f:
        f.write(f"# Problem: {target['title']}\n")
        f.write(f"# Difficulty: {target['difficulty']}\n")
        f.write(f"# Link: {target['link']}\n\n")
        f.write(clean_code)
        f.write("\n\n" + "#" * 40)
        f.write("\n# if __name__ == '__main__':\n#     s = Solution()\n#     # print(s.solve(inputs...))")
    
    # --- 3. WRITE QUESTION.MD ---
    with open(QUESTION_FILE, "w", encoding="utf-8") as f:
        f.write(f"# {target['title']}\n\n")
        f.write(f"**Difficulty:** {target['difficulty']}  \n")
        f.write(f"**Link:** [{target['link']}]({target['link']})\n\n")
        f.write("---\n\n")
        f.write("## Problem Statement\n\n")
        f.write(str(problem_text).strip() + "\n")
        
    # --- 4. WRITE EXPLANATION.MD ---
    # Added extra newlines to ensure Markdown renders cleanly in Streamlit
    with open(EXPLANATION_FILE, "w", encoding="utf-8") as f:
        f.write(f"# Professor's Analysis: {target['title']}\n\n")
        f.write(str(explanation).strip() + "\n")

    print(f"\n✅ Files Generated Successfully:\n   - {QUESTION_FILE}\n   - {SOLUTION_FILE}\n   - {EXPLANATION_FILE}")

def main():
    print("\n🟢 PROJECT GREENSCREEN: DAILY WORKFLOW STARTED")
    print("==============================================")
    
    # 1. INIT
    try:
        db = DBManager()
        loader = DSALoader(EXCEL_PATH, SHEET_NAME)
    except Exception as e:
        print(f"❌ Critical Init Failed: {e}")
        return

    # 2. SELECTION LOOP
    loader.load_all_questions()
    all_questions = loader.questions_cache
    
    completed_titles = set(db.get_completed_titles())
    candidates = [q for q in all_questions if q['title'] not in completed_titles]
    
    target = None
    print(f"🔍 Checking {len(candidates)} candidates for semantic uniqueness...")
    
    for candidate in candidates:
        is_dup, reason = db.is_duplicate(candidate['title'])
        if is_dup:
            print(f"⏭️  {reason}")
            continue 
        else:
            target = candidate
            break
            
    if not target:
        print("🎉 No new, unique questions found.")
        return

    print(f"\n🎯 TARGET LOCKED: {target['title']} ({target['difficulty']})")
    print(f"🔗 Link: {target['link']}")

    # 3. INITIALIZE AGENTS
    print("\n🤖 Waking up the AI Team...")
    researcher = get_researcher_agent()
    architect = get_architect_agent()
    engineer = get_engineer_agent()
    professor = get_professor_agent()

    # 4. EXECUTE PIPELINE
    print("📋 Assigning Tasks...")
    t1 = get_research_task(researcher, target)
    t2 = get_architect_task(architect, raw_text="Analyze the raw content provided by the Tech Researcher above.")
    t3 = get_coding_task(engineer, problem_description="Use the clean Problem Statement provided by the Problem Architect above.")
    t4 = get_analysis_task(professor, code_solution="Analyze the Python code provided by the Senior Python Engineer above.")

    print("\n🚀 Launching Crew...")
    crew = Crew(
        agents=[researcher, architect, engineer, professor],
        tasks=[t1, t2, t3, t4],
        process=Process.sequential,
        verbose=True
    )
    result = crew.kickoff()

    # 5. SAVE RESULTS
    print("\n💾 Saving Data...")
    
    # Save standard files
    save_to_files(target, t2.output.raw, t3.output.raw, t4.output.raw)
    
    # Save Agent Structured Logs
    save_agent_logs([t1, t2, t3, t4])

    # Save to Postgres
    payload = {
        "title": target['title'],
        "topic": target.get('topic', 'Algorithms'),
        "difficulty": target['difficulty'],
        "link": target['link'],
        "json_content": {
            "problem_statement": t2.output.raw,
            "solution_code": t3.output.raw,
            "explanation": t4.output.raw
        }
    }
    db.save_question(payload)
    db.close()
    
    print("\n🏁 DAILY WORKFLOW COMPLETE.")

if __name__ == "__main__":
    main()