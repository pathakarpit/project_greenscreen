from crewai import Crew, Process
from dotenv import load_dotenv

# Import your actual agents
from agents.researcher import get_researcher_agent, get_research_task
from agents.architect import get_architect_agent, get_architect_task

load_dotenv()

def main():
    print("\n🔗 STARTING INTEGRATION TEST: RESEARCHER -> ARCHITECT")
    
    # 1. SETUP THE TARGET
    # We use the title that we know works from your previous test
    target = {
        "title": "Two Sum",
        "link": "https://leetcode.com/problems/two-sum/" # This will fail, trigger fallback, and find GFG
    }

    # 2. RUN RESEARCHER (Step 1)
    print("\n🕵️ PHASE 1: RESEARCHER RUNNING...")
    researcher = get_researcher_agent()
    task_research = get_research_task(researcher, target)
    
    crew_research = Crew(
        agents=[researcher],
        tasks=[task_research]
    )
    raw_web_data = crew_research.kickoff()
    
    print("\n✅ PHASE 1 COMPLETE. Raw Data Size:", len(str(raw_web_data)), "chars")
    # print(f"Snippet: {str(raw_web_data)[:300]}...") 

    # 3. RUN ARCHITECT (Step 2)
    # We pass the 'raw_web_data' directly into the Architect's task
    print("\n🏗️ PHASE 2: ARCHITECT RUNNING...")
    architect = get_architect_agent()
    task_architect = get_architect_task(architect, str(raw_web_data))
    
    crew_architect = Crew(
        agents=[architect],
        tasks=[task_architect]
    )
    clean_structure = crew_architect.kickoff()

    # 4. FINAL OUTPUT
    print("\n" + "="*40)
    print("🏁 FINAL INTEGRATED OUTPUT")
    print("="*40)
    print(clean_structure)

if __name__ == "__main__":
    main()