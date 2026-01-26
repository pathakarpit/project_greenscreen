import os
from crewai import Agent, Task, LLM
from dotenv import load_dotenv

load_dotenv()

def get_engineer_agent():
    local_llm = LLM(
        model=os.getenv("MODEL_ENGINEER", "ollama/deepseek-coder-v2"),
        base_url="http://localhost:11434"
    )

    return Agent(
        role='Senior Python Engineer',
        goal='Write production-grade Python solutions.',
        backstory='You are a Google L5 Engineer. You write Brute Force solutions first, then Optimized O(n) solutions.',
        verbose=True,
        llm=local_llm
    )

def get_coding_task(agent, problem_description):
    return Task(
        description=f"""
        You are given a coding problem. Write a clean, executable Python file.
        
        PROBLEM:
        {problem_description}
        
        REQUIREMENTS:
        1. Define a class named `Solution`.
        2. Implement a method `solve`.
        3. Provide an Optimized (O(n) or O(log n)) approach.
        
        STRICT OUTPUT RULES (VIOLATION = FAIL):
        1. NO PREAMBLE. Do not say "Here is the code".
        2. NO POSTSCRIPT. Do not explain the code.
        3. NO MARKDOWN TICKS. Do not use ```python or ```.
        4. START DIRECTLY with "class Solution".
        5. OUTPUT ONLY VALID PYTHON CODE.
        """,
        expected_output="Valid Python code string starting with 'class Solution'.",
        agent=agent
    )

# --- TEST ---
if __name__ == "__main__":
    print("👨‍💻 Testing Engineer...")
    agent = get_engineer_agent()
    # Dummy input representing Architect output
    dummy_prob = "Given array [2,7,11,15], target 9. Return true if pair exists."
    
    from crewai import Crew
    task = get_coding_task(agent, dummy_prob)
    crew = Crew(agents=[agent], tasks=[task])
    print(crew.kickoff())