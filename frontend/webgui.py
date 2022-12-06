import streamlit as st
from backend import functions

tasks = functions.get_tasks()

st.title("My Tasks App")
st.subheader("My Task to Complete.")

for task in tasks:
    st.checkbox(task)

st.text_input(label="",placeholder="Enter a Task")