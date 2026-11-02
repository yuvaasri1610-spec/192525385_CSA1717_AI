def vacuum_cleaner():
    rooms = {"A": "Dirty", "B": "Dirty"}
    position = "A"

    print("Initial state:", rooms)

    while "Dirty" in rooms.values():
        if rooms[position] == "Dirty":
            print("Suck dirt in room", position)
            rooms[position] = "Clean"
        else:
            position = "B" if position == "A" else "A"
            print("Move to room", position)

    print("Final state:", rooms)
    print("Both rooms are clean.")

vacuum_cleaner()
