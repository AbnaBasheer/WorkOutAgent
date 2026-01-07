import os
# Fix for SIGTERM/SIGINT thread errors
os.environ["OTEL_SDK_DISABLED"] = "true"
os.environ["CREWAI_TELEMETRY_OPT_OUT"] = "true"

import streamlit as st
import profile
from crew import run_intake_step

# Page Config
st.set_page_config(page_title="Helix AI | Health Portal", layout="centered")

# --- UI State Management ---
if "step" not in st.session_state:
    st.session_state.step = 1
if "profile_data" not in st.session_state:
    st.session_state.profile_data = profile.user_profile.copy()
if "final_plan" not in st.session_state:
    st.session_state.final_plan = None

# Sync profile.py with Streamlit memory
profile.user_profile = st.session_state.profile_data

# Modern Dim Design CSS
st.markdown("""
    <style>
    .stApp { background-color: #121212; color: #E0E0E0; }
    .stButton>button { border-radius: 5px; background-color: #2E7D32; color: white; border: none; height: 3em; width: 100%;}
    .stTextInput>div>div>input, .stNumberInput>div>div>input, .stTextArea>div>div>textarea, .stSelectbox>div>div>div {
        background-color: #1E1E1E !important; color: white !important; border: 1px solid #333 !important;
    }
    .plan-box { background-color: #1E1E1E; padding: 20px; border-radius: 10px; border: 1px solid #333; line-height: 1.6; }
    header, footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- Sidebar Controls ---
with st.sidebar:
    st.title("🧬 Helix Controls")
    st.info(f"Current Step: {st.session_state.step} of 2")
    
    # Correct placement for a reset button (Outside of any main form)
    if st.button("🔄 Reset & Start Over"):
        for key in st.session_state.profile_data:
            st.session_state.profile_data[key] = None
        st.session_state.step = 1
        st.session_state.final_plan = None
        st.rerun()

st.title("Helix Health Portal")

# --- STEP 1: PHYSICAL PROFILE ---
if st.session_state.step == 1:
    with st.form("bio_form"):
        st.subheader("Step 1: Physical Profile")
        col1, col2 = st.columns(2)
        with col1:
            age = st.number_input("Age", min_value=1, value=25)
            height = st.number_input("Height (cm)", min_value=50, value=175)
        with col2:
            weight = st.number_input("Weight (kg)", min_value=10, value=75)
            goal = st.selectbox("Goal", ["Weight Loss", "Muscle Gain", "Endurance", "General Fitness"])
        
        medical = st.text_area("Medical Conditions / Medications", placeholder="e.g. None, or specific injuries")
        
        # Use st.form_submit_button ONLY inside st.form
        submit_step_1 = st.form_submit_button("Next: Set Training Preferences")
        
        if submit_step_1:
            st.session_state.profile_data.update({
                "age": age, "height": height, "weight": weight, "goal": goal,
                "medical_conditions": medical
            })
            st.session_state.step = 2
            st.rerun()

# --- STEP 2: LIFESTYLE & PREFERENCES ---
elif st.session_state.step == 2:
    if st.session_state.final_plan is None:
        with st.form("pref_form"):
            st.subheader("Step 2: Training Environment")
            
            days = st.slider("Workout days per week", 1, 7, 4)
            time_per_day = st.selectbox("Session Duration", ["15-30 mins", "30-45 mins", "45-60 mins", "60+ mins"])
            
            colA, colB = st.columns(2)
            with colA:
                location = st.radio("Location", ["Gym", "Home", "Outdoor"])
            with colB:
                equipment = st.radio("Equipment", ["Full Gym", "Basic (Dumbbells)", "None (Bodyweight)"])

            generate_clicked = st.form_submit_button("Generate My Personalized Plan")

            if generate_clicked:
                lifestyle_context = f"Days: {days}, Duration: {time_per_day}, Location: {location}, Equipment: {equipment}"
                full_input = f"Profile: {st.session_state.profile_data}. Preferences: {lifestyle_context}"
                
                with st.status("🚀 Helix AI is calculating your routine...", expanded=True) as status:
                    st.write("Cross-referencing fitness knowledge...")
                    plan = run_intake_step(full_input)
                    st.session_state.final_plan = plan
                    status.update(label="Analysis Complete!", state="complete")
                st.rerun()
    
    # Display the final plan outside the form once it's generated
    if st.session_state.final_plan:
        st.markdown("---")
        st.subheader("📋 Your Personalized Strategy")
        st.markdown(f'<div class="plan-box">{st.session_state.final_plan}</div>', unsafe_allow_html=True)
        st.download_button("Download Plan (.txt)", st.session_state.final_plan, file_name="helix_plan.txt")