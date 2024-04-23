import random
import time

import streamlit as st
import plotly.express as px
import pandas as pd

st.title("Realtime Dashboard")

def get_data():
    data = {}
    data['num'] = random.randint(1, 100)
    data['dt'] = pd.Timestamp.now()
    return data

df = pd.DataFrame([get_data()])

threshold = st.slider("Threshold", 0, 100, 0)

placeholder = st.empty()
while True:
    with placeholder.container():
        row = get_data()
        df = pd.concat([df, pd.DataFrame([row])])

        df = df[df['num'] > threshold]
        
        # pop the first row if we have more than 10
        if len(df) > 10:
            df = df.iloc[1:]

        if len(df):
            st.metric("Random Number", df['num'].iloc[-1])
            fig = px.line(df, x='dt', y='num')
            st.plotly_chart(fig)
            time.sleep(2)

    