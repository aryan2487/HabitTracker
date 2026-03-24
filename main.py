import csv
import os
from datetime import date

# Configuration
FILENAME = "productivity_data.csv"
HEADERS = ["Date", "Sleep_Hours", "DSA_Solved", "Focus_Level"]


def initialize_file():
    """Creates the CSV file with headers if it doesn't exist."""
    if not os.path.exists(FILENAME):
        with open(FILENAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(HEADERS)


def log_daily_data():
    """Prompts the user for data and saves it to the CSV."""
    today = date.today().strftime("%Y-%m-%d")
    print(f"\n--- Entry for {today} ---")

    try:
        sleep = float(input("How many hours did you sleep last night? "))
        dsa = int(input("How many DSA problems did you solve today? "))
        focus = int(input("Rate your focus/energy level today (1-10): "))

        with open(FILENAME, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([today, sleep, dsa, focus])

        print("\n✅ Data saved successfully!")
    except ValueError:
        print("\n❌ Error: Please enter valid numbers (e.g., 7.5 or 3).")


def view_insights():
    """Reads the CSV and calculates averages and correlations."""
    if not os.path.exists(FILENAME):
        print("\n❌ No data found. Log some stats first!")
        return

    sleep_data = []
    dsa_data = []

    with open(FILENAME, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            sleep_data.append(float(row["Sleep_Hours"]))
            dsa_data.append(int(row["DSA_Solved"]))

    if not sleep_data:
        print("\n❌ The file is empty. Add your first entry!")
        return

    # Calculate Averages
    avg_sleep = sum(sleep_data) / len(sleep_data)
    avg_dsa = sum(dsa_data) / len(dsa_data)

    print("\n" + "=" * 30)
    print("      YOUR ANALYTICS")
    print("=" * 30)
    print(f"Total Days Tracked: {len(sleep_data)}")
    print(f"Average Sleep:      {avg_sleep:.1f} hours")
    print(f"Average DSA Solved: {avg_dsa:.1f} problems")
    print("-" * 30)

    # Simple Logic-Based Insights (The "Problem Solver")
    if avg_sleep < 7:
        print("💡 INSIGHT: Your average sleep is below 7 hours. This usually leads to burnout.")

    if avg_dsa < 2 and avg_sleep < 6:
        print("💡 TREND: Low sleep seems to be limiting your DSA progress. Try prioritizing rest.")
    elif avg_dsa >= 3:
        print("💡 TREND: You are on a roll with DSA! Keep maintaining this rhythm.")

    print("=" * 30)


def main_menu():
    """The main control loop of the program."""
    initialize_file()

    while True:
        print("\n--- HABIT TRACKER MENU ---")
        print("1. Log Today's Stats")
        print("2. View Analysis & Insights")
        print("3. Exit")

        choice = input("\nSelect an option (1-3): ")

        if choice == "1":
            log_daily_data()
        elif choice == "2":
            view_insights()
        elif choice == "3":
            print("Keep coding and stay healthy! Goodbye.")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")


if __name__ == "__main__":
    main_menu()