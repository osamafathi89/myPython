def show_menu():
    print("1. Add Task  ")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")


def save_tasks(tasks):
    with open("revision/tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")


def load_tasks():
    tasks = []
    try:
        with open("revision/tasks.txt", "r") as file:
            tasks = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        pass
    return tasks


def delete_task(tasks, task_number):
    if task_number > 0 and task_number <= len(tasks):
        removed_task = tasks.pop(task_number-1)
        print(f"Remove Task {removed_task} has been deleted.")
        save_tasks(tasks)


def main():
    tasks = load_tasks()
    while True:
        show_menu()
        choice = input("Choose an option: ")
        if choice == "1":
            print("Enter you task ")
            task = input('Task :')
            tasks.append(task)
            save_tasks(tasks)
            print("Current Tasks:")
            for idx, t in enumerate(tasks, 1):
                print(f"{idx}. {t}")
        elif choice == "2":
            print("Current Tasks: ")
            for idx, i in enumerate(tasks, 1):
                print(f"{idx}. {i}")
        elif choice == "3":
            print("Current Tasks: ")
            for idx, i in enumerate(tasks, 1):
                print(f"{idx}. {i}")
            try:
                task_number = int(input("Enter the number of removed task : "))
            except ValueError:
                print("Please enter a valid number.")
                continue
            delete_task(tasks, task_number)
        elif choice == "4":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
