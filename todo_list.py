class Task:
    def __init__(self, description, status='Pending'):
        self.description = description
        self.status = status

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)

    def list_tasks(self):
        return [task.description for task in self.tasks]

    def mark_task_complete(self, description):
        for task in self.tasks:
            if task.description == description:
                task.status = 'Complete'

    def delete_task(self, description):
        self.tasks = [task for task in self.tasks if task.description != description]

    def clear_list(self):
        self.tasks = []
