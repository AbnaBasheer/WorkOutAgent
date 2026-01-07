from crewai import Task
from agent import intake_specialist_agent, workout_planner_agent, diet_planner_agent, reviewer_agent

def create_intake_task(user_input):
    return Task(
        # In task.py, update the description to:
        description = f"""User Input: {user_input}. 
            Extract data into JSON. If the user provides Age, Height, Weight, and Goal, 
            set 'follow_up' to null. Only provide a 'follow_up' if a CRITICAL piece 
            of data is missing.""",
        expected_output = "JSON with profile updates or follow-up questions.",
        agent = intake_specialist_agent
    )

def create_workout_plan_task(profile, context):
    return Task(
        description = f"""User Profile: {profile}. Relevant fitness knowledge: {context}. Create a personalized workout plan based on the user's health information and fitness goals.""",
        expected_output = "A detailed workout plan including exercise types, intensity, duration, and frequency.",
        agent = workout_planner_agent
    )

def create_diet_plan_task(profile, context):
    return Task(
        description = f"""User Profile: {profile}. Relevant nutrition knowledge: {context}. Create a personalized diet plan that complements the user's workout plan and supports their overall health and fitness goals.""",
        expected_output = "A detailed diet plan including meal recommendations, nutritional guidelines, and dietary preferences.",
        agent = diet_planner_agent
    )

def create_review_task():
    return Task(
        description = "Review and refine the workout and diet plans to ensure clarity, coherence, and effectiveness.",
        expected_output = "A refined and well-structured workout and diet plan ready for user implementation.",
        agent = reviewer_agent
    )