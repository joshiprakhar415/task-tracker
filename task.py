import json
import os
from datetime import date

from streamlit import status

file = "tasks.json"

class TaskManager:

    # Loading tasks
    @staticmethod
    def load_tasks():
        if not os.path.exists(file):
            return []

        with open(file, "r") as f:
            return json.load(f)

    # Saving tasks
    @staticmethod
    def save_tasks(tasks):
        with open(file, "w") as f:
            json.dump(tasks, f, indent=4)

    # Add task
    @staticmethod
    def add_task():
        tasks = TaskManager.load_tasks()

        title = input("Enter task title: ")
        description = input("Enter task description: ")
        Cdate = str(date.today())
        Udate = str(date.today())

        task_data = {
            "id": len(tasks) + 1,
            "title": title,
            "description": description,
            "status": "Pending",
            "created_at": Cdate,
            "updated_at": Udate,
        }

        tasks.append(task_data)
        TaskManager.save_tasks(tasks)

        print("Task added successfully!")

    # View tasks
    @staticmethod
    def view_tasks():
        tasks = TaskManager.load_tasks()

        if not tasks:
            print("No tasks found.")
            return

        for t in tasks:
            print("\nID:", t["id"])
            print("Title:", t["title"])
            print("Description:", t["description"])
            print("Status:", t["status"])
            print("Created_at:", t["created_at"])
            print("Updated_at:", t["updated_at"])

    # View tasks by status
    @staticmethod
    def view_tasks_by_status():
        tasks = TaskManager.load_tasks()

        if not tasks:
            print("No tasks found.")
            return

        while True:
            choice = input("Enter status to filter (1.Todo/2.In Progress/3.Done): ")
            if choice == "1":
                status = "Todo"
                break
            elif choice == "2":
                status = "In Progress"
                break
            elif choice == "3": 
                status = "Done"
                break
            else:
                print("Invalid choice")
                continue
        
        filtered_tasks = [t for t in tasks if t["status"] == status]

        if not filtered_tasks:
            print("No tasks found with the specified status.")
            return

        for t in filtered_tasks:
            print("\nID:", t["id"])
            print("Title:", t["title"])
            print("Description:", t["description"])
            print("Status:", t["status"])
            print("Created_at:", t["created_at"])
            print("Updated_at:", t["updated_at"])


    # Update task
    @staticmethod
    def update_task():
        tasks = TaskManager.load_tasks()

        task_id = int(input("Enter task ID to update: "))

        for t in tasks:
            if t["id"] == task_id:
                t["title"] = input("Enter new title: ")
                t["description"] = input("Enter new description: ")
                while True:
                    choice= input("Enter status (1.Todo/2.In Progress/3.Done): ")
                    if choice == "1":
                        t["status"] = "Todo"
                        break
                    elif choice == "2":
                        t["status"] = "In Progress"
                        break
                    elif choice == "3": 
                        t["status"] = "Done"
                        break
                    else:
                        print("Invalid choice")
                        continue

                t["updated_at"] = str(date.today())
                TaskManager.save_tasks(tasks)
                print("Task updated successfully!")
                return

        print("Task not found.")

    # Update task status
    @staticmethod
    def update_task_status():
        tasks = TaskManager.load_tasks()

        task_id = int(input("Enter task ID to update status: "))

        for t in tasks:
            if t["id"] == task_id:

                print("\nCurrent Task Details:")
                print("Title:", t["title"])
                print("Description:", t["description"])
                print("Current Status:", t["status"])
                print("Created_at:", t["created_at"])
                while True:
                    choice= input("Enter status (1.Todo/2.In Progress/3.Done): ")
                    if choice == "1":
                        t["status"] = "Todo"
                        break
                    elif choice == "2":
                        t["status"] = "In Progress"
                        break
                    elif choice == "3": 
                        t["status"] = "Done"
                        break
                    else:
                        print("Invalid choice")
                        continue
                t["updated_at"] = str(date.today())
                TaskManager.save_tasks(tasks)
                print("Task status updated successfully!")
                return

        print("Task not found.")

    # Delete task
    @staticmethod
    def delete_task():
        tasks = TaskManager.load_tasks()

        task_id = int(input("Enter task ID to delete: "))

        for t in tasks:
            if t["id"] == task_id:
                tasks.remove(t)
                TaskManager.save_tasks(tasks)
                print("Task deleted successfully!")
                return

        print("Task not found.")

    # Menu
    @staticmethod
    def main():
        while True:
            print("\n--- TASK TRACKER ---")
            print("1. Add Task")
            print("2. View Tasks by status")
            print("3. View All Tasks")
            print("4. Update Task")
            print("5. Update Task Status")
            print("6. Delete Task")
            print("7. Exit")

            choice = input("Enter choice: ")

            if choice == "1":
                TaskManager.add_task()

            elif choice == "2":
                TaskManager.view_tasks_by_status()

            elif choice == "3":
                TaskManager.view_tasks()

            elif choice == "4":
                TaskManager.update_task()
            
            elif choice == "5":
                TaskManager.update_task_status()

            elif choice == "6":
                TaskManager.delete_task()

            elif choice == "7":
                break

            else:
                print("Invalid choice")


if __name__ == "__main__":
    TaskManager.main()