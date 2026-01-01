class TaskManger:
    FILE_PATH = "revision/todo-oop/tasks.txt"

    def __init__(self, description):
        self.description = description

    def show_tasks(self):
        with open(TaskManger.FILE_PATH, "r") as file:
            tasks = [line.strip() for line in file.readlines()]
            for idx, task in enumerate(tasks, 1):
                print(f"{idx}. {task}")
        return tasks

    def add_task(self):
        tasks = self.show_tasks()
        tasks.append(self.description)
        for task in tasks:
            with open(TaskManger.FILE_PATH, "w") as file:
                file.write(task + "\n")
        print("Task added successfully.")
        self.show_tasks()

    def delete_task(self, task_number):
        tasks = self.show_tasks()
        if task_number > 0 and task_number <= len(tasks):
            removed_task = tasks.pop(task_number-1)
            print(f"Remove Task {removed_task} has been deleted.")
            with open(TaskManger.FILE_PATH, "w") as file:
                for task in tasks:
                    file.write(task + "\n")
            self.show_tasks()
