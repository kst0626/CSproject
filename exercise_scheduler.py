import json
from datetime import datetime

def save_schedule(schedule):
    with open("schedule.json", "w") as f:
        json.dump(schedule, f, indent=4, ensure_ascii=False)

def load_schedule():
    try:
        with open("schedule.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def add_exercise(schedule, exercise, date):
    schedule.append({"exercise": exercise, "date": date})
    save_schedule(schedule)

def view_schedule(schedule):
    if not schedule:
        print("No scheduled exercises.")
        return

    for entry in schedule:
        print(f"{entry['date']}: {entry['exercise']}")

def remove_exercise(schedule, date):
    new_schedule = [entry for entry in schedule if entry['date'] != date]
    save_schedule(new_schedule)
    return new_schedule

def main():
    schedule = load_schedule()
    
    while True:
        print("\n1. Add Exercise\n2. View Schedule\n3. Remove Exercise\n4. Quit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            exercise = input("Enter exercise description: ")
            date = input("Enter date (YYYY-MM-DD): ")
            add_exercise(schedule, exercise, date)
            print(f"Added exercise: {exercise} on {date}")
        
        elif choice == '2':
            print("Scheduled exercises:")
            view_schedule(schedule)
        
        elif choice == '3':
            date = input("Enter the date of the exercise to remove (YYYY-MM-DD): ")
            schedule = remove_exercise(schedule, date)
            print(f"Removed exercises on {date}")
        
        elif choice == '4':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
