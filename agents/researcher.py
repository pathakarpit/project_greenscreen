import os
import requests
from bs4 import BeautifulSoup
from crewai import Agent, Task, LLM
from crewai.tools import BaseTool
# CHANGED: Import SearchResults to get Links, not just text
from langchain_community.tools import DuckDuckGoSearchResults 
from dotenv import load_dotenv

load_dotenv()

# --- 1. CUSTOM SEARCH TOOL (Now returns Links!) ---
class SearchTool(BaseTool):
    name: str = "Internet Search"
    description: str = "Search the web for a topic. Returns a list of results with Snippets and Links."

    def _run(self, query: str) -> str:
        # This returns JSON-like output: [ {'snippet': '...', 'link': '...'}, ... ]
        tool = DuckDuckGoSearchResults()
        return tool.run(query)

# --- 2. CUSTOM SCRAPER TOOL ---
class SimpleScrapeTool(BaseTool):
    name: str = "Website Scraper"
    description: str = "Reads the content of a URL and returns the text."

    def _run(self, url: str) -> str:
        try:
            # Use a 'Real Browser' User-Agent to avoid 403 blocks
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
            }
            # verify=False prevents SSL errors on some corporate networks/WSL setups
            response = requests.get(url, headers=headers, timeout=15)
            
            if response.status_code != 200:
                return f"Error: Failed to load page (Status {response.status_code})"

            # Parse HTML
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Remove scripts, styles, navbars to clean up text
            for script in soup(["script", "style", "nav", "footer", "header", "aside"]):
                script.extract()
            
            # Get text and clean up whitespace
            text = soup.get_text()
            lines = (line.strip() for line in text.splitlines())
            clean_text = '\n'.join(chunk for chunk in lines if chunk)
            
            return clean_text[:8000] # Limit to 8k chars
            
        except Exception as e:
            return f"Error scraping website: {str(e)}"

# --- AGENT DEFINITION ---
def get_researcher_agent():
    local_llm = LLM(
        model=os.getenv("MODEL_RESEARCHER", "ollama/llama3.1"),
        base_url="http://localhost:11434"
    )

    return Agent(
        role='Tech Researcher',
        goal='Extract clean problem requirements from a webpage.',
        backstory='Expert at bypassing CSS/HTML clutter to find the core Algorithmic Problem Statement.',
        tools=[SimpleScrapeTool(), SearchTool()],
        verbose=True,
        llm=local_llm 
    )

def get_research_task(agent, target):
    return Task(
        description=f"""
        1. Try to access the Official URL: {target['link']}
        2. If that fails (403/404), use 'Internet Search' to find: "{target['title']} geeksforgeeks problem".
        3. CRITICAL: The search results will contain 'link' fields. COPY one of those links exactly. DO NOT GUESS A URL.
        4. CRITICAL: When searching, ignore pages like "Complete Guide", "Syllabus", "GATE Notes", or "file list".
        5. Look for specific tutorial pages, e.g., containing "algorithm", "problem", or "tutorial" in the title.
        6. Use 'Website Scraper' on that new link.
        7. Extract:
           - Problem Statement.
           - At least 3 Input/Output Examples.
           - Constraints.
        """,
        expected_output="Raw text containing problem details from a valid source.",
        agent=agent
    )

# --- STANDALONE TEST ---
if __name__ == "__main__":
    print("🧪 Testing Researcher Agent (Fixed URL Search)...")
    
    # We intentionally use a target that might block bots to force the fallback logic
    dummy_target = {
        "link": "https://leetcode.com/problems/two-sum/",
        "title": "Two Sum"
    }

    try:
        agent = get_researcher_agent()
        print("✅ Researcher Agent Initialized.")
    except Exception as e:
        print(f"❌ Agent Init Failed: {e}")
        exit()

    from crewai import Crew
    print("🚀 Running Task...")
    
    test_crew = Crew(agents=[agent], tasks=[get_research_task(agent, dummy_target)])
    result = test_crew.kickoff()
    
    print("\n" + "="*40)
    print("RESULT:")
    print("="*40)
    print(result)