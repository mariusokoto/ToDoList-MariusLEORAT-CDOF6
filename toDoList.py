import sys

class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def mark_complete(self):
        self.completed = True

class TaskTracker:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        self.tasks.append(Task(description))
        print(f"Task added: {description}")

    def delete_task(self, task_id):
        if 0 <= task_id < len(self.tasks):
            removed_task = self.tasks.pop(task_id)
            print(f"Task deleted: {removed_task.description}")
        else:
            print("Invalid task ID.")

    def complete_task(self, task_id):
        if 0 <= task_id < len(self.tasks):
            self.tasks[task_id].mark_complete()
            print(f"Task completed: {self.tasks[task_id].description}")
        else:
            print("Invalid task ID.")

    def modify_task(self, task_id, new_description):
        if 0 <= task_id < len(self.tasks):
            self.tasks[task_id].description = new_description
            print(f"Task modified: {new_description}")
        else:
            print("Invalid task ID.")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return

        print("\nTasks:")
        for i, task in enumerate(self.tasks):
            status = "[Completed]" if task.completed else "[Pending]"
            print(f"{i}. {task.description} {status}")

    def run(self):
        print("Task Tracker Application")
        while True:
            print("\nOptions:")
            print("1. Add Task")
            print("2. Delete Task")
            print("3. Complete Task")
            print("4. Modify Task")  # Nouvelle option
            print("5. List Tasks")
            print("6. Exit")

            try:
                choice = int(input("Enter your choice: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            if choice == 1:
                description = input("Enter task description: ")
                self.add_task(description)
            elif choice == 2:
                try:
                    task_id = int(input("Enter task ID to delete: "))
                    self.delete_task(task_id)
                except ValueError:
                    print("Invalid input. Please enter a number.")
            elif choice == 3:
                try:
                    task_id = int(input("Enter task ID to complete: "))
                    self.complete_task(task_id)
                except ValueError:
                    print("Invalid input. Please enter a number.")
            elif choice == 4:  # Nouvelle option
                try:
                    task_id = int(input("Enter task ID to modify: "))
                    new_description = input("Enter the new task description: ")
                    self.modify_task(task_id, new_description)
                except ValueError:
                    print("Invalid input. Please enter a number.")
            elif choice == 5:
                self.list_tasks()
            elif choice == 6:
                print("Exiting Task Tracker. Goodbye!")
                sys.exit()
            else:
                print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    tracker = TaskTracker()
    tracker.run()
