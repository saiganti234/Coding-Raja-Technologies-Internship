import pickle

# Define task dictionary structure
task_dict = {
    "description": "",
    "status": "incomplete",
    "priority": None,
    "due_date": None,
    "category": None,
}

# Load existing tasks from file (optional)
try:
    with open("tasks.dat", "rb") as f:
        tasks = pickle.load(f)
except FileNotFoundError:
    tasks = []

# Helper functions

def display_tasks(tasks, filter_key=None, filter_value=None):
    for i, task in enumerate(tasks):
        if filter_key is not None and filter_value != task[filter_key]:
            continue
        print(f"{i+1}. {task['description']} ({task['status']})")
        if task['priority']:
            print(f"    Priority: {task['priority']}")
        if task['due_date']:
            print(f"    Due Date: {task['due_date']}")
        if task['category']:
            print(f"    Category: {task['category']}")
        print("")

def get_task_number(prompt):
    while True:
        try:
            number = int(input(prompt))
            if number > 0 and number <= len(tasks):
                return number - 1
            else:
                print("Invalid task number. Please enter a valid number between 1 and", len(tasks))
        except ValueError:
            print("Invalid input. Please enter a number.")


# Main program loop
print('Yours To-Do List Needs To Be Focused On You')
while True:
    command = input("Enter command in numericals(1.add, 2.list, 3.complete, 4.delete, 5.help, 6.exit): ").lower().strip()

    if command== "1":
        description = input("Enter task description or name: ")
        priority = input("Enter priority (high, medium, low): ").lower().strip()
        due_date = input("Enter due date (DD-MM-YYYY): ")
        category = input("Enter category: ")
        new_task = {**task_dict}
        new_task["description"] = description
        new_task["priority"] = priority if priority else None
        new_task["due_date"] = due_date if due_date else None
        new_task["category"] = category if category else None
        tasks.append(new_task)
        print("Task added successfully!")

    elif command == "2":
        filter_by = input("Filter by (status, category, all): ").lower().strip()
        filter_value = None
        if filter_by == "status":
            filter_value = input("Enter status (completed, incomplete): ").lower().strip()
        elif filter_by == "category":
            filter_value = input("Enter category: ")
        display_tasks(tasks, filter_by, filter_value)

    elif command == "3":
        task_number = get_task_number("Enter task number to complete: ")
        tasks[task_number]["status"] = "completed"
        print("Task marked as completed!")

    elif command == "4":
        task_number = get_task_number("Enter task number to delete: ")
        del tasks[task_number]
        print("Task deleted successfully!")

    elif command == "5":
        print("Available commands:")
        print("- add: Add a new task")
        print("- list: List all tasks (optionally filtered by status or category)")
        print("- complete: Mark a task as completed")
        print("- delete: Delete a task")
        print("- help: Display this help message")
        print("- exit: Quit the application")

    elif command == "6":
        # Save tasks to file (optional)
        with open("tasks.dat", "wb") as f:
            pickle.dump(tasks, f)
        print("Exiting...")
        break

    else:
        print("Invalid command. Please try again.")


