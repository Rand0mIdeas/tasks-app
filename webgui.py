import streamlit as st
import functions

tasks = functions.get_tasks()

def add_task():
    task = st.session_state["new_task"] + "\n"
    tasks.append(task)
    functions.write_tasks(tasks)


st.title("My Tasks App")
st.subheader("My Task to Complete.")

for index, task in enumerate(tasks):
    checkbox = st.checkbox(task, key=task)
    if checkbox:
        tasks.pop(index)
        functions.write_tasks(tasks)
        del st.session_state[task]
        st.experimental_rerun()

st.text_input(label="", placeholder="Enter a Task",
              on_change=add_task, key="new_task")
