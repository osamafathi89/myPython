
def main():
    Task = __import__("revision.todo-oop.taskmange").TaskManger
    while True:
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            task_desc = input("Enter your task: ")
            task = Task(task_desc)
            task.add_task()
        elif choice == "2":
            Task.show_tasks()
        elif choice == "3":
            Task.show_tasks()
            try:
                task_number = int(input("Enter the number of removed task : "))
            except ValueError:
                print("Please enter a valid number.")
                continue
            task = Task("")
            task.delete_task(task_number)
        elif choice == "4":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
