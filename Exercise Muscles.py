print("Welcome to Strength Max!")

# Step 1: Choose goal
print("\nWhat is your fitness goal?")
print("1. Build muscle")
print("2. Lose weight")
print("3. Body recomp")

goal_choice = input("\nEnter 1, 2, or 3: ")

if goal_choice == "1":
    goal = "Build muscle"

    # Step 2: Choose muscle group
    print("\nSelect a muscle group:")
    print("1. Chest")
    print("2. Back")
    print("3. Biceps")
    print("4. Triceps")
    print("5. Shoulders")

    muscle_choice = input("\nEnter 1–5: ")

    if muscle_choice == "1":
        muscle = "Chest"
        exercises = [
            "Pec Fly",
            "Bench Press",
            "Incline Press",
            "Dumbbell Incline Press"
        ]

    elif muscle_choice == "2":
        muscle = "Back"
        exercises = [
            "Cable Pulldowns",
            "Cable Rows",
            "Single Arm Pulldown"
        ]

    elif muscle_choice == "3":
        muscle = "Biceps"
        exercises = [
            "Incline Curls",
            "Preacher Curls",
            "Hammer Curls"
        ]

    elif muscle_choice == "4":
        muscle = "Triceps"
        exercises = [
            "Skull Crushers",
            "Dips",
            "Overhead Tricep Extension"
        ]

    elif muscle_choice == "5":
        muscle = "Shoulders"
        exercises = [
            "Smith Machine Shoulder Press",
            "Shoulder Shrugs",
            "Upright Row"
        ]

    else:
        print("Invalid muscle choice.")
        exit()

    # Step 3: Output workout
    print(f"\nGoal: {goal}")
    print(f"Muscle Group: {muscle}")

    print("\nWorkout Plan:")
    for ex in exercises:
        print(f"- {ex}: 2 sets to failure (increase weight on second set)")

elif goal_choice == "2":
    print("\nLose weight program coming soon...")

elif goal_choice == "3":
    print("\nBody recomp program coming soon...")

else:
    print("\nInvalid choice. Restart program.")