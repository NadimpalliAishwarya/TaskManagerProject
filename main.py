from db import initialize_db
from crud import add_task, view_tasks, update_task, delete_task

def main():

    initialize_db()
    
    while True:
        print("==== Task Manager ====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task Status")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            update_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print(" Exiting Task Manager.")
            break
        else:
            print(" Invalid choice. Please try again.\n")

if __name__ == '__main__':
    main()
