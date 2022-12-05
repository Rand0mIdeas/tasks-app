import time
import functions
import PySimpleGUI as sg
import os

if not os.path.exists("tasks.txt"):
    with open("tasks.txt", "w") as file:
        pass

sg.theme("DarkBlue4")

clock = sg.Text('', key="clock")
label = sg.Text("Enter a task:")
input_box = sg.InputText(tooltip="Enter a Task:", key='task')
add_button = sg.Button("Add", size=10, tooltip="Add Task")
list_box = sg.Listbox(values=functions.get_tasks(), key="tasks",
                      enable_events=True, size=[46, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button(image_source="complete.png", tooltip="Completes selected task", key="Complete")
exit_button = sg.Button("Exit")

window = sg.Window("My Tasks App",
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button],
                           [complete_button],
                           [exit_button]],
                   font=("Helvetica", 12))

while True:
    event, values = window.read(timeout=1000)
    window["clock"].update(value=time.strftime("%d %b %Y %H:%M:%S"))

    match event:
        case "Add":
            tasks = functions.get_tasks()
            new_task = values['task'] + "\n"
            tasks.append(new_task)
            functions.write_tasks(tasks)
            window['tasks'].update(values=tasks)

        case "Edit":
            try:
                task_to_edit = values['tasks'][0]
                new_task = values['task']

                tasks = functions.get_tasks()
                index = tasks.index(task_to_edit)
                tasks[index] = new_task
                functions.write_tasks(tasks)
                window['tasks'].update(values=tasks)
            except IndexError:
                sg.popup("Please select a task task to edit", font=("Helvetica", 10))

        case "Complete":
            try:
                task_to_complete = values['tasks'][0]
                tasks = functions.get_tasks()
                tasks.remove(task_to_complete)
                functions.write_tasks(tasks)
                window['tasks'].update(values=tasks)
                window['task'].update(value='')
            except IndexError:
                sg.popup("Please select a task to complete", font=("Helvetica", 10))

        case "Exit":
            break

        case "tasks":
            window['task'].update(value=values['tasks'][0])

        case sg.WINDOW_CLOSED:
            break

window.close()
