import json
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

def calculate_completion_rate(tasks):
    '''
    Return percent of completed task
    '''
    # TODO
    completed_tasks = sum(1 for task in tasks if task['completed'])
    total_tasks = len(tasks)
    
    if total_tasks == 0:
        return 0  # Trả về 0, tránh chia 0 => Lỗi
    
    completion_rate = (completed_tasks / total_tasks) * 100
    return completion_rate

def analyze_task_distribution(tasks):
    '''
    Return number of task distribute by category
    '''
    # TODO
    distribution = {}
    for task in tasks:
        category = task['category']
        if category in distribution:
            distribution[category] += 1
        else:
            distribution[category] = 1
    return distribution

def calculate_average_completion_time(tasks):
    '''
    Return average of day to finish the date, calculate by taking all task 
    '''
    # TODO
    total_days = 0
    completed_tasks_count = 0

    for task in tasks:
        if task['completed']:
            add_date = datetime.strptime(task['add_date'], '%Y-%m-%d')
            finished_date = datetime.strptime(task['finished_date'], '%Y-%m-%d')
            total_days += (finished_date - add_date).days
            completed_tasks_count += 1
    
    if completed_tasks_count == 0:
        return 0  # Tránh chia cho 0 nếu không có task nào hoàn thành
    
    average_completion_time = total_days / completed_tasks_count
    return average_completion_time

def identify_overdue_tasks(tasks):
    '''
    Show task not finish in time
    '''
    # TODO
    overdue_tasks = []
    current_date = datetime.now()

    for task in tasks:
        if not task['completed']:
            due_date = datetime.strptime(task['due_date'], '%Y-%m-%d')
            if current_date > due_date:
                overdue_tasks.append(task)

    return overdue_tasks

def generate_productivity_report(tasks):
    '''
    Write report to a file
    '''
    # TODO
    ...
    ...
    report = f"""
Productivity Report
-------------------
Task Completion Rate: {calculate_completion_rate(tasks)}%
Average Completion Time: {calculate_average_completion_time(tasks)} days
Number of Overdue Tasks: {len(identify_overdue_tasks(tasks))}

Task Distribution:
{analyze_task_distribution(tasks)}

Recommendations:
1. {"Great job on task completion!" if calculate_average_completion_time(tasks) > 80 else "Try to improve your task completion rate."}
2. {"Work on reducing your average completion time." if calculate_average_completion_time(tasks) > 7 else "You're completing tasks in a timely manner!"}
3. {"Focus on completing overdue tasks." if len(identify_overdue_tasks(tasks)) >= 1 else "Keep up the good work on avoiding overdue tasks!"}
"""
    with open("productivity_report.txt", "w") as f:
        f.write(report)

def plot_task_distribution(tasks):
    distribution = analyze_task_distribution(tasks)
    plt.figure(figsize=(10, 6))
    plt.bar(distribution.keys(), distribution.values())
    plt.title("Task Distribution")
    plt.xlabel("Task Categories")
    plt.ylabel("Number of Tasks")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("task_distribution.png")
    print("Task distribution plot saved as 'task_distribution.png'")

def productivity_tracker_main(tasks):
    while True:
        print("\nProductivity Tracker")
        print("1. Generate Productivity Report")
        print("2. Plot Task Distribution")
        print("3. Return to Task Management System")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            generate_productivity_report(tasks)
        elif choice == "2":
            plot_task_distribution(tasks)
        elif choice == "3":
            print("Returning to Task Management System...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    print("This module is designed to be run from the Task Management System.")
    print("Please run main.py instead.")
