import functions
import PySimpleGUI as sg

label = sg.Text("Type in a task")
input_box = sg.InputText(tooltip="Enter a Task", key="task")
add_button = sg.Button("Add")

window = sg.Window("My Tasks App",
                   layout=[[label], [input_box, add_button]],
                   font=("Helvetica", 12))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            tasks = functions.get_tasks()
            new_task = values['task'] + "\n"
            tasks.append(new_task)
            functions.write_tasks(tasks)
        case sg.WINDOW_CLOSED:
            break

window.close()
