import sys
import json
import time


if __name__ == "__main__":
    # Check if there is the file already, if not - create one
    try:
        file = open("tasks.json", "r")
    except FileNotFoundError:
        file = open("tasks.json", "w")
        file.close()
        file = open("tasks.json", "r")

    curr_time = time.strftime("%H:%M %h %d %Y")
    cli_argv = sys.argv
    command = cli_argv[1]
    n = len(cli_argv)
    commands = ["add", "update", "delete", "mark-in-progress", "mark-done", "list", ]
    task_states = ["todo", "in-progress", "done", ]

    # Catching any unwanted behaviors
    if n > 4:
        sys.exit("Hey, there is too many arguments.")
    elif n == 1:
        sys.exit("Hey, put some arguments.")
    elif command not in commands:
        sys.exit("Unknown command.")

    # Reading the content of the file
    data = file.readlines()
    file.close()

    if command != "add" and not data:
        sys.exit("No tasks found")

    if not data:
        tasks = list()
    else:
        tasks = json.loads(data[0])
    file.close()

    match command:
        case "add":
            if len(cli_argv) < 3:
                exit("More arguments please!")
            # Checking the spare id
            if not tasks:
                task_id = 1
            else:
                task_id = tasks[-1]["id"] + 1

            task_description = cli_argv[2]
            task = {
                    'id': task_id,
                    'description': task_description,
                    'status': "todo",
                    "createdAt": curr_time,
                    "updatedAt": curr_time,

                    }
            tasks.append(task)
            print(f"Output: Task added successfully (ID: {task_id})")

        case "update" | "delete" | "mark-in-progress" | "mark-done":
            task_id = cli_argv[2]
            try:
                task_id = int(task_id)
            except ValueError:
                sys.exit("Hey, id is ONLY an int")

            if task_id not in [task["id"] for task in tasks]:
                print("No tasks found")

            for task in tasks:
                if task["id"] == task_id:
                    if cli_argv[1] == "update":
                        task_description = cli_argv[3]
                        print(
                            f"Output: Task updated successfully "
                            f"(ID: {task_id}, {task['description']} --> {task_description})")
                        task["updatedAt"] = curr_time
                        task["description"] = task_description

                    elif cli_argv[1] == "delete":
                        print(f"Output: Task deleted successfully (ID: {task_id})")
                        tasks.remove(task)

                    elif cli_argv[1] == "mark-in-progress":
                        print(f"Output: Task status updated successfully "
                              f"(ID: {task_id}, {task['status']} --> 'in-progress')")
                        task["updatedAt"] = curr_time
                        task["status"] = "in-progress"

                    elif cli_argv[1] == "mark-done":
                        print(f"Output: Task status updated successfully "
                              f"(ID: {task_id}, {task['status']} --> 'done')")
                        task["updatedAt"] = curr_time
                        task["status"] = "done"

                    else:
                        print(f"HOW?\n{cli_argv}")
                    break

        case "list":
            if len(cli_argv) == 2:
                for task in tasks:
                    print(task)

            elif len(cli_argv) == 3 and cli_argv[2] in task_states:
                for task in tasks:
                    if task["status"] == cli_argv[2]:
                        print(task)
            sys.exit()

    with open("tasks.json", "w") as file:
        file.write(json.dumps(tasks))
