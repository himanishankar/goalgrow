"""Core logic for GoalGrow: create goals, add savings, track progress."""
import json
import math
import os
from datetime import date, datetime

FILENAME = "goals.json"


def load_goals(filename=FILENAME):
    if not os.path.isfile(filename):
        return []
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)


def save_goals(goals, filename=FILENAME):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(goals, f, indent=2)


def find_goal(goals, name):
    for goal in goals:
        if goal["name"].lower() == name.strip().lower():
            return goal
    return None


def create_goal(name, target, deadline, filename=FILENAME, today=None):
    """Create a new goal. Deadline format: YYYY-MM-DD."""
    today = today or date.today()
    name = name.strip()

    if not name:
        raise ValueError("Goal name cannot be empty.")
    if target <= 0:
        raise ValueError("Target amount must be positive.")
    try:
        deadline_date = datetime.strptime(deadline, "%Y-%m-%d").date()
    except ValueError:
        raise ValueError("Deadline must be in YYYY-MM-DD format.")
    if deadline_date <= today:
        raise ValueError("Deadline must be a future date.")

    goals = load_goals(filename)
    if find_goal(goals, name):
        raise ValueError("A goal with this name already exists.")

    goal = {
        "name": name,
        "target": target,
        "saved": 0.0,
        "deadline": deadline,
        "created": today.isoformat(),
    }
    goals.append(goal)
    save_goals(goals, filename)
    return goal


def add_savings(name, amount, filename=FILENAME):
    """Add money to an existing goal."""
    if amount <= 0:
        raise ValueError("Amount must be positive.")

    goals = load_goals(filename)
    goal = find_goal(goals, name)
    if goal is None:
        raise ValueError("Goal not found.")

    goal["saved"] += amount
    save_goals(goals, filename)
    return goal


def delete_goal(name, filename=FILENAME):
    goals = load_goals(filename)
    goal = find_goal(goals, name)
    if goal is None:
        raise ValueError("Goal not found.")
    goals.remove(goal)
    save_goals(goals, filename)


def months_left(deadline, today=None):
    """Months remaining until the deadline (rounded up, 0 if passed)."""
    today = today or date.today()
    deadline_date = datetime.strptime(deadline, "%Y-%m-%d").date()
    days = (deadline_date - today).days
    if days <= 0:
        return 0
    return max(1, math.ceil(days / 30.44))


def monthly_required(goal, today=None):
    """Amount to save every month to reach the goal on time."""
    remaining = max(goal["target"] - goal["saved"], 0)
    if remaining == 0:
        return 0.0
    months = months_left(goal["deadline"], today)
    if months == 0:
        return remaining
    return remaining / months


def progress_percent(goal):
    return min(goal["saved"] / goal["target"] * 100, 100)


def progress_bar(percent, width=20):
    filled = int(percent / 100 * width)
    return "#" * filled + "-" * (width - filled)