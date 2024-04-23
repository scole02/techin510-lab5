import datetime
import zoneinfo
import time

import streamlit as st

cols = st.columns(3)
with cols[0]:
    st.write("Timezone 1")
    timezone1 = st.selectbox("Select a timezone", zoneinfo.available_timezones(), key="timezone1")

with cols[1]:
    st.write("Timezone 2")
    timezone2 = st.selectbox("Select a timezone", zoneinfo.available_timezones(), key="timezone2")

with cols[2]:
    st.write("Timezone 3")
    timezone3 = st.selectbox("Select a timezone", zoneinfo.available_timezones(), key="timezone3")

placeholder = st.empty()

while True:
    with placeholder.container():
        st.write(int(time.time()))
        cols = st.columns(3)
        with cols[0]:
            st.write(datetime.datetime.now(zoneinfo.ZoneInfo(timezone1)))
        
        with cols[1]:
            st.write(datetime.datetime.now(zoneinfo.ZoneInfo(timezone2)))

        with cols[2]:
            st.write(datetime.datetime.now(zoneinfo.ZoneInfo(timezone3)))

        time.sleep(1)