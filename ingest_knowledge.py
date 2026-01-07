import os
from tavily import TavilyClient
from dotenv import load_dotenv

load_dotenv()

def fetch_and_save_knowledge():
    tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))
    
    # Define topics to build a comprehensive fitness library
    queries = [
        "progressive overload principles for muscle gain",
        "optimal protein intake for fat loss while preserving muscle",
        "low-impact exercises for people with knee or back pain",
        "differences between full body, upper/lower, and PPL splits",
        "nutritional guidelines for endurance athletes",
        "home workout equipment alternatives for compound movements"
    ]
    
    knowledge_path = "data/knowledge.txt"
    os.makedirs("data", exist_ok=True)

    print("🚀 Gathering fitness knowledge...")

    with open(knowledge_path, "a", encoding="utf-8") as f:
        for query in queries:
            print(f"Searching for: {query}")
            # Get search results with content snippets
            response = tavily.search(query=query, search_depth="advanced", max_results=3)
            
            for result in response['results']:
                content = result['content']
                # Clean and write to file
                f.write(f"\nSOURCE: {result['url']}\n")
                f.write(f"{content}\n")
                f.write("-" * 30 + "\n")
                
    print(f"✅ Knowledge base updated in {knowledge_path}")

if __name__ == "__main__":
    fetch_and_save_knowledge()