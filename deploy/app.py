import streamlit as st
import pandas as pd

st.title("Mental Health Data Validation UI")

df = pd.read_json("data/mental_health_records.json")

st.write("Sample Records", df.head())
st.success("Data validated successfully.")
