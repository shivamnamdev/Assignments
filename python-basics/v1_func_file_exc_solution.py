import json
import os


# ==========================================
# Create Log File
# ==========================================

def create_log_file(filename):

    try:
        file = open(filename, "x")

    except FileExistsError as e:
        print("File already exists.")
        print(e)

    except PermissionError as e:
        print("Permission denied.")
        print(e)

    else:
        print("Log file created successfully.")

    finally:
        try:
            file.close()
        except:
            pass


# ==========================================
# Add Task
# ==========================================

def add_task(filename, task_name, priority):

    try:
        file = open(filename, "a")

        task = {
            "task": task_name,
            "priority": priority
        }

        file.write(json.dumps(task) + "\n")

    except FileNotFoundError as e:
        print("Log file not found.")
        print(e)

    except IOError as e:
        print("Unable to write to file.")
        print(e)

    else:
        print("Task added successfully.")

    finally:
        try:
            file.close()
        except:
            pass


# ==========================================
# Read Tasks
# ==========================================

def read_tasks(filename):

    tasks = []

    try:
        file = open(filename, "r")

        for line in file:
            tasks.append(json.loads(line))

    except FileNotFoundError as e:
        print("File not found.")
        print(e)

    except json.JSONDecodeError as e:
        print("Invalid JSON data.")
        print(e)

    else:
        print("Tasks loaded successfully.")

    finally:
        try:
            file.close()
        except:
            pass

    return tasks


# ==========================================
# Search Task
# ==========================================

def search_task(filename, keyword):

    try:

        if keyword == "":
            raise ValueError("Keyword cannot be empty")

        file = open(filename, "r")

        found = False

        while True:

            line = file.readline()

            if not line:
                break

            task = json.loads(line)

            if keyword.lower() in task["task"].lower():
                print(task)
                found = True

        if not found:
            print("Task not found")

    except ValueError as e:
        print("Invalid input")
        print(e)

    except FileNotFoundError as e:
        print("File not found")
        print(e)

    else:
        print("Search completed")

    finally:
        try:
            file.close()
        except:
            pass


def normalize_task_name(task_name):
    return task_name.strip().lower()


# ==========================================
# Delete Task
# ==========================================

def delete_task(filename, task_name):

    try:

        tasks = read_tasks(filename)

        if normalize_task_name(task_name) == "":
            raise ValueError("Task name cannot be empty")

        input_name = normalize_task_name(task_name)

        exact_matches = [
            i for i, task in enumerate(tasks)
            if normalize_task_name(task["task"]) == input_name
        ]

        if len(exact_matches) == 1:
            del tasks[exact_matches[0]]

        elif len(exact_matches) > 1:
            del tasks[exact_matches[0]]
            print("Multiple exact matches found. Deleted first matching task.")

        else:
            partial_matches = [
                i for i, task in enumerate(tasks)
                if input_name in normalize_task_name(task["task"])
            ]

            if len(partial_matches) == 1:
                del tasks[partial_matches[0]]

            elif len(partial_matches) > 1:
                print("Multiple tasks matched. Please type a more specific name:")

                for i in partial_matches:
                    print(f"- {tasks[i]['task']}")

                raise ValueError("Ambiguous task name")

            else:
                raise KeyError("Task not found")

        file = open(filename, "w")

        for task in tasks:
            file.write(json.dumps(task) + "\n")

    except ValueError as e:
        print(e)

    except KeyError as e:
        print(e)

    except FileNotFoundError as e:
        print(e)

    else:
        print("Task deleted successfully.")

    finally:
        try:
            file.close()
        except:
            pass


# ==========================================
# Generate Report
# ==========================================

def generate_report(filename, report_file):

    try:

        tasks = read_tasks(filename)

        report = open(report_file, "w")

        report.write("TASK REPORT\n")
        report.write("=" * 30 + "\n")

        for task in tasks:

            report.write(
                f"Task: {task['task']} | Priority: {task['priority']}\n"
            )

    except FileNotFoundError as e:
        print("File not found")
        print(e)

    except PermissionError as e:
        print("Permission denied")
        print(e)

    else:
        print("Report generated successfully.")

    finally:

        try:
            report.close()
        except:
            pass

        print("Generate report operation finished.")


# ==========================================
# Main Program
# ==========================================

filename = "tasks.txt"

while True:

    try:

        print("\n===== TASK LOGGER =====")
        print("1. Create Log")
        print("2. Add Task")
        print("3. View Tasks")
        print("4. Search Task")
        print("5. Delete Task")
        print("6. Generate Report")
        print("7. Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:

            create_log_file(filename)

        elif choice == 2:

            task_name = input("Task Name: ")
            priority = input("Priority: ")

            add_task(filename, task_name, priority)

        elif choice == 3:

            tasks = read_tasks(filename)

            for task in tasks:
                print(task)

        elif choice == 4:

            keyword = input("Keyword: ")
            search_task(filename, keyword)

        elif choice == 5:

            task_name = input("Task Name to Delete: ")
            delete_task(filename, task_name)

        elif choice == 6:

            generate_report(
                filename,
                "report.txt"
            )

        elif choice == 7:

            print("Program Closed")
            break

        else:
            print("Invalid Choice")

    except ValueError as e:
        print("Please enter a valid number.")
        print(e)

    except Exception as e:
        print("Unexpected Error:")
        print(e)