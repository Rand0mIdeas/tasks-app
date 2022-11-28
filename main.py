import time
import functions


current_time = time.strftime("%d %b %Y %H:%M:%S")
print(current_time)
while True:
    user_action = input("Type add or show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        task = user_action[4:]

        tasks = functions.get_tasks()

        tasks.append(task + "\n")

        functions.write_tasks(tasks)

    elif user_action.startswith("show"):

        tasks = functions.get_tasks()

        for index, item in enumerate(tasks):
            item = item.strip("\n")
            row = f"{index + 1}. {item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            print(number)

            number = number - 1

            tasks = functions.get_tasks()

            new_task = input("Enter new task: ")
            tasks[number] = new_task + "\n"

            functions.write_tasks(tasks)
        except ValueError:
            print("That's not a valid command.")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            tasks = functions.get_tasks()
            index = number - 1
            tasks_to_remove = tasks[index].strip('\n')
            tasks.pop(index)

            functions.write_tasks(tasks)

            message = f'Task {tasks_to_remove} was removed form the list.'
            print(message)
        except ValueError:
            print("There aren't that many tasks to  complete.")
            continue

    elif user_action.startswith("exit"):
        break
    else:
        print("That's not a valid command")

print("Goodbye!")
