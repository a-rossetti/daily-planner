from utils.date_utils import get_current_date
from utils.goals_utils import GoalsManager
from utils.diary_utils import DiaryManager


def get_user_choice():
    while True:
        try:
            choice = input("> ")
            if choice not in ["1", "2", "3", "4", "5"]:
                raise ValueError("Invalid choice. Please select a number between 1 and 5.")
            return choice
        except ValueError as e:
            print(e)


def main():
    goals_manager = GoalsManager("archive/goals.txt")
    diary_manager = DiaryManager("archive/diary.txt")

    print("Daily Planner")
    print(f"Today's date is {get_current_date()}")

    while True:
        print("\nChoose an option: ")
        print("1. Write today's goals")
        print("2. Read today's goals")
        print("3. Review today's goals")
        print("4. Write a diary entry")
        print("5. Exit")

        choice = get_user_choice()

        if choice == "1":
            goals_manager.write_goals()
        elif choice == "2":
            goals_manager.read_goals()
        elif choice == "3":
            goals_manager.review_goals()
        elif choice == "4":
            diary_manager.write_entry()
        elif choice == "5":
            print("Thank you for using the daily planner!")
            break


if __name__ == "__main__":
    main()
