Teams = ["Team A", "Team B"]
Scores = [0, 0]
players = {
    "Team A": ["Player 1", "Player 2", "Player 3"],
    "Team B": ["Player 4", "Player 5", "Player 6"]
}
team_index = 0

school_soccer_itinerary = []


def add_itinerary_item():
    print("\nAdd a School Soccer Itinerary Item")
    day = input("Day: ")
    date = input("Date (YYYY-MM-DD): ")
    time = input("Time: ")
    activity = input("Activity: ")
    location = input("Location: ")
    coach = input("Coach: ")
    notes = input("Notes: ")

    item = {
        "day": day,
        "date": date,
        "time": time,
        "activity": activity,
        "location": location,
        "coach": coach,
        "notes": notes
    }
    school_soccer_itinerary.append(item)
    print("Itinerary item added!")


def team_rotation():
    global Teams
    Teams = Teams[1:] + Teams[:1]


def update_score(team_index, points):
    global Scores
    Scores[team_index] += points


def show_itinerary():
    print("School Soccer Itinerary")
    print("=" * 30)
    for item in school_soccer_itinerary:
        print(
            f"{item['day']} {item['date']} | "
            f"{item['time']} | {item['activity']} | "
            f"{item['location']} | Coach: {item['coach']}"
        )
        print(f"Notes: {item['notes']}")
        print("-" * 30)


if __name__ == "__main__":
    while True:
        add_itinerary_item()
        another = input("Add another itinerary item? (y/n): ").strip().lower()
        if another != "y":
            break

    show_itinerary()
    print(f"\nCurrent teams: {Teams}")
    print(f"Current scores: {Scores}")
