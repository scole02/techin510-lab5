import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
from os import getenv
import time

# Load environment variables and configure API
load_dotenv()
genai.configure(api_key=getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel('gemini-pro')

def generate_workout(training_level, time_approx, muscle_groups, considerations):
    prompt = f"Generate a {training_level.lower()} workout plan for {time_approx} minutes targeting {', '.join(muscle_groups)}."
    if considerations:
        prompt += f" Considerations: {considerations}"
    response = model.generate_content(prompt)
    return response.text

def app_style():
    st.markdown("""
        <style>
        .css-18e3th9 {
            background-color: #f0f2f6;
            color: #333;
        }
        .css-1d391kg {
            padding: 1rem;
            border-radius: 0.5rem;
            background-color: #ffffff;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .timer {
            font-size: 24px;
            font-weight: bold;
            color: #0078D7;
            background-color: #e0f7ff;
            padding: 10px;
            border-radius: 10px;
            display: inline-block;
        }
        </style>
        """, unsafe_allow_html=True)

def stopwatch():
    if 'time' not in st.session_state:
        st.session_state.time = 0
        st.session_state.running = False
        st.session_state.last_update_time = time.time()

    def start():
        if not st.session_state.running:
            st.session_state.running = True
            st.session_state.last_update_time = time.time()

    def pause():
        if st.session_state.running:
            st.session_state.running = False
            st.session_state.time += time.time() - st.session_state.last_update_time

    def reset():
        st.session_state.running = False
        st.session_state.time = 0

    col1, col2, col3 = st.columns(3)
    with col1:
        st.button('Start', on_click=start)
    with col2:
        st.button('Pause', on_click=pause)
    with col3:
        st.button('Reset', on_click=reset)

    if st.session_state.running:
        elapsed_time = time.time() - st.session_state.last_update_time
        display_time = st.session_state.time + elapsed_time
        st.session_state.timer_display = f'Time: {int(display_time)} seconds'
    else:
        st.session_state.timer_display = f'Time: {int(st.session_state.time)} seconds'

    st.markdown(f'<div class="timer">{st.session_state.timer_display}</div>', unsafe_allow_html=True)

    # Automatically rerun the app to update the stopwatch every second
    if st.session_state.running:
        st.rerun()

st.title('Workout Plan Generator')
app_style()  # Apply custom styles

# User inputs
training_level = st.selectbox('Select your training level:', ['Beginner', 'Intermediate', 'Advanced'])
time_approx = st.text_input('Approximate time for workout (in minutes):')
muscle_groups_list = ['Chest', 'Triceps', 'Biceps', 'Back', 'Shoulders', 
                      'Quads', 'Hamstrings', 'Glutes', 'Calves', 'Abs']
muscle_groups = st.multiselect('Select muscle groups to train:', muscle_groups_list)
considerations = st.text_area('Any additional considerations?')

if st.button('Generate Workout Plan'):
    workout_plan = generate_workout(training_level, time_approx, muscle_groups, considerations)
    st.session_state.workout_plan = workout_plan  # Store workout plan in session state

if 'workout_plan' in st.session_state:
    st.markdown(st.session_state.workout_plan)  # Display the stored workout plan

stopwatch()  # Add the stopwatch feature to the app
