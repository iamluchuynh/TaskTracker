from manager import load_tasks, add_task, list_tasks, mark_task_completed, delete_task, search_tasks, save_tasks

def display_menu():
    print("\nTask Management System")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Search Tasks")
    print("6. Productivity Tracker")
    print("7. Exit")

def main():
    tasks = load_tasks()

    while True:
        display_menu()
        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            add_task(tasks["tasks"])
        elif choice == '2':
            list_tasks(tasks["tasks"])
        elif choice == '3':
            mark_task_completed(tasks["tasks"])
        elif choice == '4':
            delete_task(tasks["tasks"])
        elif choice == '5':
            search_tasks(tasks["tasks"])
        elif choice == '6':
            productivity_tracker_menu(tasks["tasks"])
        elif choice == '7':
            print("Thank you for using the Task Management System!")
            break
        else:
            print("Invalid choice. Please try again.")

def productivity_tracker_menu(tasks):
    from tracker import productivity_tracker_main
    productivity_tracker_main(tasks)

if __name__ == "__main__":
    main()