import streamlit as st
import pandas as pd
import plotly.express as px
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "backend")))
from queries import *

st.set_page_config(page_title="Cybersecurity Log Monitor", layout="wide")

st.title("Real-Time Cybersecurity Log Dashboard")

#Auto refresh every 5 seconds
st_autorefresh=st.empty()

#Metrics
st.subheader("Overview Metrics")
col1, col2 = st.columns(2)
col1.metric("Total Logs",get_total_logs())
col2.metric("Failed Logins", get_failed_logins())

st.subheader("Top Attacking IPs")
top_ips = get_top_attacking_ips()
df_ips = pd.DataFrame(top_ips, columns=["Source IP", "Attempts"])
st.table(df_ips)

st.subheader("Events Over Time")
events = get_events_over_time()
df_events = pd.DataFrame(events, columns=["Date", "Event Count"])
fig = px.line(df_events, x="Date", y="Event Count")
st.plotly_chart(fig, use_container_width=True)

st_autorefresh.empty()
st.subheader("Brute Force Detection")

brute_force_ips = detect_brute_force()

if brute_force_ips:
    st.error("Possible Brute Force Attack Detected!")
    st.table(brute_force_ips)
else:
    st.success("No brute force activity detected.")