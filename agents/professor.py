import os
from crewai import Agent, Task, LLM
from dotenv import load_dotenv

load_dotenv()

def get_professor_agent():
    local_llm = LLM(
        model=os.getenv("MODEL_PROFESSOR", "ollama/llama3.1"),
        base_url="http://localhost:11434"
    )

    return Agent(
        role='CS Professor',
        goal='Explain the Time/Space complexity clearly.',
        backstory='You explain complex algorithms to students using diagrams and clear language.',
        verbose=True,
        llm=local_llm
    )

def get_analysis_task(agent, code_solution):
    return Task(
        description=f"""
        Analyze the following Python solution and explain it to a student.
        
        CODE TO ANALYZE:
        {code_solution}
        
        OUTPUT REQUIREMENTS:
        
        1. **Time Complexity Analysis**: 
           - State the Big O (e.g., O(N)).
           - CRITICAL: Explicitly explain that the loop runs N times and the dictionary lookup `if x in dict` takes O(1) time on average.
           - Therefore, N * O(1) = O(N).
           
        2. **Space Complexity Analysis**: 
           - State the Big O.
           - Explain that we use a dictionary/hash map to store at most N elements.
           
        3. **Step-by-Step Reconstruction Logic**:
           - Explain the logic in such detail that a developer could rewrite the code just by reading these steps.
           - Mention exactly what variables are initialized.
           - Describe the condition for the loop.
           - Describe the specific math (`target - current_num`) used to find the complement.
           - Explain the `if/else` logic: What happens if the complement IS found? What happens if it IS NOT found?
           - Mention the final return statement if no pair is found.
        
        STRICT FORMAT:
        - Do NOT output the code block again.
        - Use Markdown headers (##).
        - Use bullet points for the steps.
        """,
        expected_output="Detailed Markdown explanation allowing code reconstruction.",
        agent=agent
    )

# --- STANDALONE TEST ---
if __name__ == "__main__":
    print("🎓 Testing Professor Agent (Detailed Mode)...")
    
    dummy_code = """
    class Solution:
        def solve(self, nums, target):
            seen = {}
            for i, num in enumerate(nums):
                complement = target - num
                if complement in seen:
                    return [seen[complement], i]
                seen[num] = i
            return []
    """

    try:
        agent = get_professor_agent()
        task = get_analysis_task(agent, dummy_code)
        
        from crewai import Crew
        crew = Crew(agents=[agent], tasks=[task])
        result = crew.kickoff()
        
        print("\n" + "="*40)
        print("PROFESSOR OUTPUT:")
        print("="*40)
        print(result)
        
    except Exception as e:
        print(f"❌ Error: {e}")