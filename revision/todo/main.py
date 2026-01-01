def show_menu():
    print("1. Add Task  ")
    print("2. View Tasks")
    print("3. Exit")


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
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
