import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
from os import getenv

load_dotenv()
# Assuming you have set up authentication for Google's API elsewhere
genai.configure(api_key=getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel('gemini-pro')

def generate_workout(training_level, time_approx, muscle_groups, considerations):
    # Construct the prompt for Google Gemini
    prompt = f"Generate a {training_level.lower()} workout plan for {time_approx} minutes targeting {', '.join(muscle_groups)}."
    if considerations:
        prompt += f" Considerations: {considerations}"
    
    # Call the Google Gemini API
    response = model.generate_content(prompt)
    print(response)
    return response.text

st.title('Workout Plan Generator')

# User inputs
training_level = st.selectbox('Select your training level:', ['Beginner', 'Intermediate', 'Advanced'])
time_approx = st.text_input('Approximate time for workout (in minutes):')
muscle_groups_list = ['Chest', 'Triceps', 'Biceps', 'Back', 'Shoulders', 
                      'Quads', 'Hamstrings', 'Glutes', 'Calves', 'Abs']
muscle_groups = st.multiselect('Select muscle groups to train:', muscle_groups_list)
considerations = st.text_area('Any additional considerations?')

if st.button('Generate Workout Plan'):
    workout_plan = generate_workout(training_level, time_approx, muscle_groups, considerations)
    st.markdown(workout_plan)
