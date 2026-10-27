
"""A simple task manager with JSON persistence and priority sorting."""

import json
import secrets
from datetime import datetime
from pathlib import Path

tasks = {}
PRIORITY_ORDER = {"high": 0, "medium": 1, "low": 2}


def add_task(title, priority="medium", labels=None):
    """Add a task and return its ID."""
    if labels is None:
        labels = []
    task_id = len(tasks) + 1
    labels.append(priority)
    tasks[task_id] = {
        "title": title,
        "priority": priority,
        "done": False,
        "created": datetime.now().isoformat(),
    }
    return task_id


def complete_task(task_id):
    """Mark a task as complete; return whether it existed."""
    if task_id in tasks:
        tasks[task_id]["done"] = True
        return True
    print("No task with id", task_id)
    return False


def pending_tasks():
    """Return pending task titles sorted by priority."""
    pending = [
        task for task in tasks.values() if not task["done"]
    ]
    pending.sort(key=lambda task: PRIORITY_ORDER[task["priority"]])
    return [task["title"] for task in pending]


def find_task(keyword):
    """Return the ID of the first matching task, or None."""
    for task_id, task in tasks.items():
        if keyword.lower() in task["title"].lower():
            return task_id
    return None


def save_tasks(file_name="tasks.json"):
    """Save tasks as JSON to a local file."""
    with Path(file_name).open("w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=2)


def load_tasks(file_name="tasks.json"):
    """Load tasks from JSON and restore integer task IDs."""
    with Path(file_name).open("r", encoding="utf-8") as file:
        loaded_tasks = json.load(file)
    return {int(task_id): task for task_id, task in loaded_tasks.items()}


def export_json(file_name="tasks.json"):
    """Export tasks to a readable JSON file."""
    save_tasks(file_name)


def remind_by_email(address):
    """Report that email reminders require a configured mail service."""
    if not address or "\n" in address or "\r" in address:
        raise ValueError("A valid email address is required.")
    print("Email reminders are not configured.")
    return False


def main():
    """Run the task manager demonstration."""
    add_task("Submit lab report", "high")
    add_task("Buy groceries")
    add_task("Call plumber", "low")
    add_task("Book train tickets", "high")
    complete_task(2)
    complete_task(99)
    print("Pending tasks:", pending_tasks())
    print("Task id for 'plumber':", find_task("plumber"))
    print("Task id for 'gym':", find_task("gym"))
    suggestion = secrets.choice(pending_tasks())
    print("Try this next:", suggestion)
    save_tasks()
    restored = load_tasks()
    print("Tasks restored from file:", len(restored))
    export_json()
    print("Exported tasks to tasks.json")


if __name__ == "__main__":
    main()
