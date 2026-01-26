import sys
import os
import re
from crewai import Crew, Process
from dotenv import load_dotenv

# --- PATH SETUP ---
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from agents.researcher import get_researcher_agent, get_research_task
from agents.architect import get_architect_agent, get_architect_task
from agents.engineer import get_engineer_agent, get_coding_task
from agents.professor import get_professor_agent, get_analysis_task

load_dotenv(os.path.join(parent_dir, '.env'))

def main():
    print("\n🔗 STARTING FINAL INTEGRATION TEST (R -> A -> E -> P)")
    print("======================================================")
    
    target = {
        "title": "Two Sum",
        "link": "https://leetcode.com/problems/two-sum/" 
    }

    print("\n🤖 [1/4] Initializing Agents...")
    researcher = get_researcher_agent()
    architect = get_architect_agent()
    engineer = get_engineer_agent()
    professor = get_professor_agent()

    # --- KEY FIX: BETTER PLACEHOLDERS ---
    # We explicitly tell the agents to look at the context provided by CrewAI
    
    t1_scrape = get_research_task(researcher, target)
    
    t2_format = get_architect_task(architect, raw_text="Analyze the content provided by the Tech Researcher above.")
    
    t3_code = get_coding_task(engineer, problem_description="Use the Problem Statement provided by the Problem Architect above.")
    
    t4_explain = get_analysis_task(professor, code_solution="Analyze the Python code provided by the Senior Python Engineer above.")

    print("\n🚀 [3/4] Launching Crew...")
    crew = Crew(
        agents=[researcher, architect, engineer, professor],
        tasks=[t1_scrape, t2_format, t3_code, t4_explain],
        process=Process.sequential,
        verbose=True
    )

    result = crew.kickoff()

    print("\n\n" + "="*60)
    print("🏁 FINAL SYSTEM REPORT")
    print("="*60)

    # --- CHECK 1: RESEARCHER ---
    raw_len = len(str(t1_scrape.output.raw))
    print(f"\n[1] RESEARCHER (Web Data):")
    if raw_len > 100:
        print(f"    ✅ Success ({raw_len} chars)")
    else:
        print(f"    ❌ FAIL: Content too short")

    # --- CHECK 2: ARCHITECT ---
    prob_text = str(t2_format.output.raw)
    print(f"\n[2] ARCHITECT (Problem Statement):")
    # Fix: Looser check for "Description" and "Examples"
    if "Description" in prob_text and "Examples" in prob_text:
        print("    ✅ Success (Structure Detected)")
    else:
        print("    ⚠️ Warning: Output structure unclear.")

    # --- CHECK 3: ENGINEER ---
    code_text = str(t3_code.output.raw)
    print(f"\n[3] ENGINEER (Solution Code):")
    
    if "class Solution" in code_text:
        print("    ✅ Success (Valid Class Definition)")
    else:
        print("    ❌ FAIL: No 'class Solution' found.")
    
    # Check if prompt injection worked (No markdown ticks)
    if "```" not in code_text:
        print("    ✅ Strict Mode: Perfect (No Markdown)")
    else:
        print("    ⚠️ Strict Mode: Failed (Markdown present)")

    # --- CHECK 4: PROFESSOR ---
    expl_text = str(t4_explain.output.raw)
    print(f"\n[4] PROFESSOR (Explanation):")
    
    # Fix: Robust checks for Complexity Analysis
    has_time = any(x in expl_text for x in ["Time Complexity", "O(N)", "O(n)"])
    has_space = any(x in expl_text for x in ["Space Complexity", "Memory"])
    
    if has_time and has_space:
        print("    ✅ Success: Complexity Analysis Found")
    else:
        print("    ❌ FAIL: Complexity Analysis Missing")

    if "Step" in expl_text or "1." in expl_text:
        print("    ✅ Success: Logic Steps Found")
    else:
        print("    ⚠️ Warning: Logic steps might be missing.")

    print("\n" + "="*60)

if __name__ == "__main__":
    main()