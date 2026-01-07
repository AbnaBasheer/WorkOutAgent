from crewai import Agent
from crewai_tools import TavilySearchTool
from crewai.llm import LLM
from dotenv import load_dotenv
import os

load_dotenv()

llm = LLM(
    model = "gemini-2.5-flash",
    gemini_api_key = os.getenv("GEMINI_API_KEY"),
    temperature = 0.3
)

search_tool = TavilySearchTool(
    tavily_api_key = os.getenv("TAVILY_API_KEY"),
    max_results = 3
)

intake_specialist_agent = Agent(
    role = "Health Intake Specialist",
    goal = "Collect and understand the user's health and fitness data safely.",
    backstory = """You ask relevant health questions. You never give medical advice.""",
    llm = llm,
    verbose = False
)

workout_planner_agent = Agent(
    role = "Workout Planner",
    goal = "Create a safe and personalized workout plans based on the user's health information and fitness goals.",
    backstory = """You create workouts based on goals, health constraints and retrieved fitness knowledge. You can use tools when necessary""",
    tools = [search_tool],
    llm = llm,
    verbose = False
)

diet_planner_agent = Agent(
    role = "Diet Planner",
    goal = "To provide dietary recommendations that complement the user's workout plan and support their overall health and fitness goals.",
    backstory = """You provide general nutrition advice, not medical prescriptions.""",
    tools = [search_tool],
    llm = llm,
    verbose = False
)

reviewer_agent = Agent(
    role = "Workout and Diet Plan Reviewer",
    goal = "Ensure plans are safe, realistic and well-structured.",
    backstory = """ You review the workout and diet plans to ensure that it is safe, realistic and well-structured inorder to avoid unsafe recommendations.""",
    llm = llm,
    verbose = False
)