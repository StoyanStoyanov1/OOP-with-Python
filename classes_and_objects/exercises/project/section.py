from oop.classes_and_objects.exercises.tо_do_list.project.task import Task


class Section:

    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"

        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name):
        for current_task in self.tasks:
            if current_task.name == task_name:
                current_task.completed = True
                return f"Completed task {task_name}"

        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        amount_of_removed_tasks = 0
        for current_task in self.tasks:
            if current_task.completed:
                amount_of_removed_tasks += 1
                self.tasks.remove(current_task)

        return f"Cleared {amount_of_removed_tasks} tasks."

    def view_section(self):
        result = [f"Section {self.name}:"]

        for task in self.tasks:
            result.append(task.details())

        return '\n'.join(result)

task = Task("Make bed", "27/05/2020")
print(task.change_name("Go to University"))
print(task.change_due_date("28.05.2020"))
task.add_comment("Don't forget laptop")
print(task.edit_comment(0, "Don't forget laptop and notebook"))
print(task.details())
section = Section("Daily tasks")
print(section.add_task(task))
second_task = Task("Make bed", "27/05/2020")
section.add_task(second_task)
print(section.clean_section())
print(section.view_section())
