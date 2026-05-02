elif goal_choice == "2":
    goal = "Lose weight"

    print("\nChoose your workout:")
    print("1. Upper Body")
    print("2. Legs")
    print("3. Upper Body 2")
    print("4. Core")

    choice = input("\nEnter 1, 2, 3, or 4: ")

    if choice == "1":
        workout = "Upper Body"
        exercises = [
            "Diamond Push Ups",
            "Plate on Back Push Ups",
            "Slow Controlled Push Ups",
            "Side to Side Push Ups",
            "Pike Push Ups",
            "Chair Dips"
        ]
        sets_reps = "3 sets of 10-12 reps"

    elif choice == "2":
        workout = "Legs"
        exercises = [
            "Bulgarian Leg Squats",
            "Single Leg Toe Touches",
            "Standing Calf Raises",
            "Reverse Step Lunges",
            "Glute Bridges"
        ]
        sets_reps = "3 sets of 10-12 reps"

    elif choice == "3":
        workout = "Upper Body 2"
        exercises = [
            "Chin Ups",
            "Pull Ups",
            "Inverted Barbell Row",
            "Inverted Bicep Curl",
            "Close Grip Pull Up"
        ]
        sets_reps = "3 sets of 10 reps"

    elif choice == "4":
        workout = "Core"
        exercises = [
            "Planks",
            "Toe Touches",
            "Russian Twists",
            "Bicycle Crunches"
        ]
        sets_reps = "3 sets of 1 minute"

    else:
        print("Invalid choice.")
        exit()

    print(f"\nGoal: {goal}")
    print(f"Workout Type: {workout}")

    print("\nWorkout Plan:")
    for ex in exercises:
        print(f"- {ex}: {sets_reps}")