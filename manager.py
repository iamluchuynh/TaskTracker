import os
import json
from datetime import datetime, timedelta

TASKS_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    return {"tasks": []}

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump({"tasks": tasks}, file, indent=2)

def add_task(tasks):
    '''
    Show all task
    task = {
        "id": 
        "title": 
        "category": 
        "description":
        "add_date"
        "due_date": 
        "finished_date": 
        "completed": 
    }
    '''
    # TODO: Fill here
    if isinstance(tasks, dict) and "tasks" in tasks:
        tasks_list = tasks["tasks"]
    else:
        tasks_list = tasks

    task_id = len(tasks_list) + 1        # task_id trước đó + 1
    title = input("Enter the task title: ")
    category = input("Enter the task category: ")
    description = input("Enter the task description: ")
    add_date = datetime.now().strftime("%Y-%m-%d")                  
    due_date = input("Enter the due date (YYYY-MM-DD): ")
    task = {
        "id": task_id,
        "title": title,
        "category": category,
        "description": description,
        "add_date": add_date,
        "due_date": due_date,
        "finished_date": None,
        "completed": False
    }
    tasks_list.append(task)
    save_tasks(tasks)
    print(f"Task '{title}' was added successfully!")
    

def list_tasks(tasks):
    '''
    Show all task
    '''
    # TODO: Fill here
    if isinstance(tasks, dict) and "tasks" in tasks:
        tasks_list = tasks["tasks"]
    else:
        tasks_list = tasks

    if len(tasks_list) == 0:
        print("There aren't any available tasks")
    else:
        for task in tasks_list:
            status = "Completed" if task["completed"] else "Incompleted"
            print(f"ID: {task['id']}, Title: {task['title']}, Status: {status}")

def mark_task_completed(tasks):
    '''
    Change state of the task to complete and add finish date
    '''
    task_id = int(input("Enter the ID of the task to mark as completed: "))
    # TODO: Fill here
    if isinstance(tasks, dict) and "tasks" in tasks:
        tasks_list = tasks["tasks"]
    else:
        tasks_list = tasks

    for task in tasks_list:
        if task["id"] == task_id:
            task["completed"] = True
            task["finished_date"] = datetime.now().strftime("%Y-%m-%d")
            task_found = True
            print(f"Task '{task['title']}' was marked as completed.")
            break
    if not task_found:
        print(f"Task with ID {task_id} not found.")
        
    save_tasks(tasks)

def delete_task(tasks):
    '''
    Delete a task
    '''
    task_id = int(input("Enter the ID of the task to delete: "))
    # TODO: Fill here
    if isinstance(tasks, dict) and "tasks" in tasks:
        tasks_list = tasks["tasks"]
    else:
        tasks_list = tasks

    task_found = False
    for task in tasks_list:
        if task["id"] == task_id:
            tasks_list.remove(task)
            task_found = True
            print(f"Task '{task['title']}' was deleted")
            break
    if not task_found:
        print(f"Task with ID {task_id} not found.")
    save_tasks(tasks)

def search_tasks(tasks):
    '''
    Find task by keyword, check the keyword is inside description, title or id 
    '''
    keyword = input("Enter a keyword to search for: ").lower()
    # TODO: Fill here
    if isinstance(tasks, dict) and "tasks" in tasks:
        tasks_list = tasks["tasks"]
    else:
        tasks_list = tasks
    found_tasks = [task for task in tasks_list if keyword in task["title"].lower() or keyword in task["description"].lower()]
    if found_tasks:
        for task in found_tasks:
            print(f"ID: {task['id']}, Title: {task['title']}, Description: {task['description']}")
    else:
        print("No tasks found matching the keyword you have provided")