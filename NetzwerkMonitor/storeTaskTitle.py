class Task:
    def __init__(self, title):
        self.title = title
        self.is_completed = False  # Tasks start as pending

    def complete(self):
        self.is_completed = True


def main():
    # 1. Initialize our task collection list
    task_list = [
        Task("Buy groceries"),
        Task("Finish Python lesson"),
        Task("Clean workspace"),
    ]

    # 2. Simulate completing one task
    task_list[1].complete()  # Finishes the Python lesson!

    # 3. Use a List Comprehension to filter for only pending tasks
    pending_tasks = [t for t in task_list if not t.is_completed]

    # 4. Display the results
    print("--- PENDING TASKS ---")
    for task in pending_tasks:
        print(f"[ ] {task.title}")


# Run the script
if __name__ == "__main__":
    main()
