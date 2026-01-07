
🏋️ AI Fitness Coach (Multi-Agent System)
📌 Project Overview

This project is an AI-powered fitness coaching system built using CrewAI and Google Gemini.
It uses multiple specialized AI agents to safely collect user health data, generate personalized workout plans, recommend complementary diet guidance, and review outputs for safety and realism.

The system focuses on general fitness and wellness and does not provide medical advice.

🎯 Key Features

Multi-agent architecture using CrewAI

Personalized workout planning

General diet recommendations aligned with workouts

Safety-focused plan review

Web search integration for up-to-date fitness knowledge

No medical diagnosis or prescriptions

🤖 Agents Used
Agent	Responsibility
Health Intake Specialist	Collects user fitness and health information safely
Workout Planner	Creates personalized workout routines
Diet Planner	Provides general nutrition guidance
Reviewer	Validates safety, realism, and structure
🧠 Architecture (High Level)

User provides health and fitness details

Intake Agent collects and structures data

Workout Planner generates workout plan

Diet Planner suggests diet support

Reviewer Agent validates the final output

🛠️ Tech Stack

Python

CrewAI

Google Gemini (gemini-2.5-flash)

Tavily Search Tool

dotenv

🔐 Environment Setup
1️⃣ Clone the Repository
git clone https://github.com/your-username/ai-fitness-coach.git
cd ai-fitness-coach

2️⃣ Create Virtual Environment
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Configure Environment Variables

Create a .env file:

GEMINI_API_KEY=your_gemini_api_key
TAVILY_API_KEY=your_tavily_api_key

▶️ How to Run
python main.py

⚠️ Disclaimer

This application provides general fitness and nutrition guidance only.
It does not provide medical advice, diagnosis, or treatment.
Always consult a healthcare professional for medical concerns.


🚀 Future Improvements

RAG with WHO and fitness guidelines

Lifestyle & sleep planning agent

User progress tracking

Frontend UI (Streamlit / Web App)

Wearable data integration

⭐ Why This Project?

Demonstrates Agentic AI

Shows responsible AI design

Strong portfolio project for AI / ML roles
