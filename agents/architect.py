import os
from crewai import Agent, Task, LLM
from dotenv import load_dotenv

load_dotenv()

def get_architect_agent():
    # Explicit Local LLM definition
    local_llm = LLM(
        model=os.getenv("MODEL_ARCHITECT", "ollama/llama3.1"),
        base_url="http://localhost:11434"
    )

    return Agent(
        role='Problem Architect',
        goal='Create a standardized Exam Question format.',
        backstory='You take raw, messy web scrapes and format them into clear, professional algorithmic problems.',
        verbose=True,
        llm=local_llm
    )

def get_architect_task(agent, raw_text):
    return Task(
        description=f"""
        You are given raw text scraped from a coding website. It is messy and may contain multiple solutions (C++, Java, etc.).
        
        YOUR JOB:
        1. Extract the core **Problem Statement**.
        2. Extract or Create 3 clear **Input/Output Examples**.
        3. Define the **Constraints** (if missing, invent reasonable ones, e.g., 1 <= N <= 10^5).
        4. REMOVE any solution code (C++, Python implementations) found in the text. We only want the *Question*.
        
        RAW TEXT INPUT:
        {raw_text}
        """,
        expected_output="A structured string containing: Title, Description, Examples, and Constraints.",
        agent=agent
    )

# --- STANDALONE TEST ---
if __name__ == "__main__":
    print("🏗️ Testing Architect Agent...")
    
    # 1. Simulate the output we just got from the Researcher
    dummy_raw_text = """
    2 Sum - Count Pairs with given Sum. 
    Given an array arr[] = [-1, 1, 5, 5, 7], target = 6. 
    Output: 3. Explanation: Pairs are (1,5), (1,5), (-1,7).
    
    C++ Code:
    int countPairs(vector<int> &arr, int target) { ... }
    """

    try:
        agent = get_architect_agent()
        print("✅ Architect Agent Initialized.")
    except Exception as e:
        print(f"❌ Init Failed: {e}")
        exit()

    from crewai import Crew
    
    task = get_architect_task(agent, dummy_raw_text)
    crew = Crew(agents=[agent], tasks=[task])
    
    print("🚀 Formatting Problem...")
    result = crew.kickoff()
    
    print("\n" + "="*40)
    print("ARCHITECT OUTPUT:")
    print("="*40)
    print(result)