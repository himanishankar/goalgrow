"""GoalGrow - Set a goal. Save smart. Watch it grow."""
import sys

from goals import (
    add_savings, create_goal, delete_goal, load_goals,
    monthly_required, months_left, progress_bar, progress_percent,
)

# Lets the ₹ symbol print correctly on Windows terminals
sys.stdout.reconfigure(encoding="utf-8")


def read_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def create_goal_menu():
    name = input("Goal name (e.g. Laptop): ")
    target = read_float("Target amount (₹): ")
    deadline = input("Deadline (YYYY-MM-DD): ").strip()
    try:
        create_goal(name, target, deadline)
        print("Goal created!")
    except ValueError as e:
        print(f"Error: {e}")


def add_savings_menu():
    name = input("Which goal? ")
    amount = read_float("Amount saved (₹): ")
    try:
        goal = add_savings(name, amount)
        print(f"Added! You have now saved ₹{goal['saved']:,.2f} of ₹{goal['target']:,.2f}.")
    except ValueError as e:
        print(f"Error: {e}")


def view_goals_menu():
    goals = load_goals()
    if not goals:
        print("No goals yet. Create one first.")
        return

    for g in goals:
        percent = progress_percent(g)
        left = months_left(g["deadline"])
        print(f"\nGoal: {g['name']}")
        print(f"   [{progress_bar(percent)}] {percent:.1f}%")
        print(f"   Saved ₹{g['saved']:,.2f} of ₹{g['target']:,.2f}")
        print(f"   Deadline: {g['deadline']} ({left} months left)")

        if g["saved"] >= g["target"]:
            print("   Goal achieved! Congratulations!")
        elif left == 0:
            print(f"   Deadline passed. ₹{monthly_required(g):,.2f} still needed.")
        else:
            print(f"   Save ₹{monthly_required(g):,.2f} per month to reach it on time.")


def delete_goal_menu():
    name = input("Which goal to delete? ")
    try:
        delete_goal(name)
        print("Goal deleted.")
    except ValueError as e:
        print(f"Error: {e}")


def main():
    options = {
        "1": ("Create a goal", create_goal_menu),
        "2": ("Add savings", add_savings_menu),
        "3": ("View my goals", view_goals_menu),
        "4": ("Delete a goal", delete_goal_menu),
    }
    while True:
        print("\n=== GoalGrow ===")
        for key, (label, _) in options.items():
            print(f"{key}. {label}")
        print("5. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "5":
            print("Keep saving. Goodbye!")
            break
        if choice in options:
            options[choice][1]()
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()