import sys
import os
from dotenv import load_dotenv
from crewai import Crew, Process

# --- 1. SETUP PATHS (CRITICAL FIX) ---
# This tells Python: "Look for modules in the folder one level up (..)"
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

# Now we can import from the main project folders
from agents.researcher import get_researcher_agent, get_research_task
from agents.architect import get_architect_agent, get_architect_task
from agents.engineer import get_engineer_agent, get_coding_task

# Load .env from the parent directory
load_dotenv(os.path.join(parent_dir, '.env'))

def main():
    print("\n🔗 STARTING FULL PIPELINE TEST: RESEARCHER -> ARCHITECT -> ENGINEER")
    
    # 2. SETUP TARGET
    # We use a standard problem to ensure consistent results
    target = {
        "title": "Two Sum",
        "link": "https://leetcode.com/problems/two-sum/" 
        # Note: This link might fail (403), triggering the Researcher's fallback logic.
    }

    # 3. INITIALIZE AGENTS
    print("\n🤖 Initializing Agents...")
    try:
        researcher = get_researcher_agent()
        architect = get_architect_agent()
        engineer = get_engineer_agent()
    except Exception as e:
        print(f"❌ Failed to initialize agents: {e}")
        return

    # 4. DEFINE TASKS
    # The output of t1 (Raw Text) -> input of t2
    # The output of t2 (Clean Prob) -> input of t3
    t1_scrape = get_research_task(researcher, target)
    t2_format = get_architect_task(architect, raw_text="Wait for previous task output")
    t3_code = get_coding_task(engineer, problem_description="Wait for previous task output")

    # 5. RUN CREW
    print("\n🚀 Kickoff! This may take 1-2 minutes...")
    crew = Crew(
        agents=[researcher, architect, engineer],
        tasks=[t1_scrape, t2_format, t3_code],
        process=Process.sequential,
        verbose=True
    )

    # CrewAI returns the output of the *last* task in the list
    final_output = crew.kickoff()

    # 6. INSPECT RESULTS
    print("\n" + "="*50)
    print("🏁 PIPELINE REPORT")
    print("="*50)

    # Researcher Output
    if t1_scrape.output:
        print(f"\n[1] RESEARCHER OUTPUT (Raw Data):")
        print(f"    Length: {len(str(t1_scrape.output.raw))} chars")
    else:
        print("\n[1] RESEARCHER OUTPUT: None")

    # Architect Output
    if t2_format.output:
        print(f"\n[2] ARCHITECT OUTPUT (Clean Problem):")
        print(f"    Length: {len(str(t2_format.output.raw))} chars")
        print("-" * 20)
        print(str(t2_format.output.raw)[:300] + "...\n(truncated)")
        print("-" * 20)
    else:
        print("\n[2] ARCHITECT OUTPUT: None")

    # Engineer Output
    if t3_code.output:
        print(f"\n[3] ENGINEER OUTPUT (Python Code):")
        print("-" * 20)
        print(t3_code.output.raw)
        print("-" * 20)

        # 7. VALIDATION
        if "class Solution" in str(t3_code.output.raw) and "def" in str(t3_code.output.raw):
            print("\n✅ SUCCESS: Valid Python class structure detected.")
        else:
            print("\n❌ WARNING: Output does not look like standard Solution class code.")
    else:
        print("\n[3] ENGINEER OUTPUT: None")

if __name__ == "__main__":
    main()