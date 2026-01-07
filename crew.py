from crewai import Crew
from agent import intake_specialist_agent, workout_planner_agent, diet_planner_agent, reviewer_agent
from task import create_intake_task, create_workout_plan_task, create_diet_plan_task, create_review_task
from profile import update_profile, is_profile_complete, profile_summary
from rag import load_knowledge, retrieve_context
import json

load_knowledge()

def run_intake_step(user_input: str) -> str:
    # Use the Specialist to parse the large string into JSON
    intake_task = create_intake_task(user_input)
    intake_crew = Crew(agents=[intake_specialist_agent], tasks=[intake_task])
    
    # We bypass the 'is_profile_complete' logic because Step 2 provides 
    # the info even if the AI doesn't parse it perfectly.
    context = retrieve_context(user_input) # Get RAG data based on the whole input
    
    workout_plan_task = create_workout_plan_task(user_input, context)
    diet_plan_task = create_diet_plan_task(user_input, context)
    review_task = create_review_task()
    
    planning_crew = Crew(
        agents=[workout_planner_agent, diet_planner_agent, reviewer_agent],
        tasks=[workout_plan_task, diet_plan_task, review_task],
        verbose=False
    )
    
    response = planning_crew.kickoff()
    return response.raw