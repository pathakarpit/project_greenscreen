import os
import re
from google import genai
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
model_name = os.getenv("MODEL_ID")

# Configuration
API_KEY = api_key
MODEL_ID = model_name

if not api_key:
    raise ValueError("GEMINI_API_KEY not found! Check your .env file.")

def solve_and_save_dsa(problem_name):
    # Initialize the client
    client = genai.Client(api_key=API_KEY)
    
    # We ask for specific delimiters to make parsing easy
    prompt = (
        f"Solve the following DSA problem: {problem_name}. "
        "Provide your output exactly in this format:\n"
        "START_QUESTION\n[The problem description]\nEND_QUESTION\n"
        "START_CODE\n[The Python code solution]\nEND_CODE\n"
        "Do not use markdown formatting like triple backticks."
    )

    try:
        print(f"Requesting solution for: {problem_name}...")
        response = client.models.generate_content(
            model=MODEL_ID,
            contents=prompt
        )
        text = response.text

        # Extract Question and Code using Regex
        question_match = re.search(r"START_QUESTION\n(.*?)\nEND_QUESTION", text, re.DOTALL)
        code_match = re.search(r"START_CODE\n(.*?)\nEND_CODE", text, re.DOTALL)

        if question_match and code_match:
            question_content = question_match.group(1).strip()
            code_content = code_match.group(1).strip()

            # Create filenames based on the problem name
            base_name = problem_name.lower().replace(" ", "_")
            
            # Save Question
            with open(f"{base_name}_problem.txt", "w") as f:
                f.write(question_content)
            
            # Save Code
            with open(f"{base_name}_solution.py", "w") as f:
                f.write(code_content)

            print(f"✅ Success! Created {base_name}_problem.txt and {base_name}_solution.py")
        else:
            print("❌ Error: Could not parse the response correctly.")
            print("Raw Response:", text)

    except Exception as e:
        print(f"❌ API Error: {e}")

if __name__ == "__main__":
    # Example: solve 'Longest Substring Without Repeating Characters'
    solve_and_save_dsa("Valid Parentheses")