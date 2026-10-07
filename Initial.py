from dataclasses import dataclass, field


@dataclass
class Task:
    title: str
    priority: int
    completed: bool = False


@dataclass
class Project:
    name: str
    tasks: list[Task] = field(default_factory=list)

    def add_task(self, title: str, priority: int):
        self.tasks.append(Task(title, priority))

    def complete_task(self, title: str):
        for task in self.tasks:
            if task.title.lower() == title.lower():
                task.completed = True

    def progress(self) -> float:
        if not self.tasks:
            return 0.0

        completed = sum(task.completed for task in self.tasks)
        return completed / len(self.tasks) * 100

    def report(self):
        print(f"Project: {self.name}")
        print("=" * (9 + len(self.name)))

        for task in sorted(self.tasks, key=lambda item: item.priority, reverse=True):
            status = "Done" if task.completed else "Open"
            print(f"[{status}] {task.title} | Priority: {task.priority}")

        print(f"\nProgress: {self.progress():.1f}%")


project = Project("Website Redesign")

project.add_task("Create layout", 5)
project.add_task("Build navigation", 4)
project.add_task("Add authentication", 5)
project.add_task("Optimize images", 2)
project.add_task("Deploy website", 3)

project.complete_task("Create layout")
project.complete_task("Build navigation")
project.complete_task("Optimize images")

project.report()