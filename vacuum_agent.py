# Simple PEAS-Based Smart Vacuum Cleaner Agent

rooms = {
    "Room A": "Dirty",
    "Room B": "Clean",
    "Room C": "Dirty",
    "Room D": "Clean"
}

print("Smart Vacuum Cleaner Agent")
print("--------------------------")

for room, condition in rooms.items():

    print("\nCurrent Room:", room)
    print("Condition:", condition)

    if condition == "Dirty":
        print("Action: Cleaning", room)
        rooms[room] = "Clean"
    else:
        print("Action: Room is already clean")
        print("Action: Moving to next room")

print("\nFinal Room Conditions:")
for room, condition in rooms.items():
    print(room, ":", condition)

print("\nAgent task completed successfully.")
