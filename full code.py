print("\nWhat is your fitness goal?")
print("1. Build muscle")
print("2. Lose weight")
print("3. Body recomp")
print("4. Dictionary")

goal_choice = input("\nEnter 1, 2, 3, or 4: ")

# ---------------- BUILD MUSCLE ---------------- #
if goal_choice == "1":
    goal = "Build muscle"

    # Step 2: Muscle group that they will be choosing to work on
    print("\nSelect a muscle group:")
    print("1. Chest")
    print("2. Back")
    print("3. Biceps")
    print("4. Triceps")
    print("5. Shoulders")
    print("6. Legs")

    muscle_choice = input("\nEnter 1–6: ")

    # Exercise muscle choices for the chest
    if muscle_choice == "1":
        muscle = "Chest"
        exercises = [
            "Pec Fly",
            "Bench Press",
            "Incline Press",
            "Dumbbell Incline Press"
        ]

    # Exercise choices for the back
    elif muscle_choice == "2":
        muscle = "Back"
        exercises = [
            "Cable Pulldowns",
            "Cable Rows",
            "Single Arm Pulldown"
        ]

    # Exercise choices for the biceps
    elif muscle_choice == "3":
        muscle = "Biceps"
        exercises = [
            "Incline Curls",
            "Preacher Curls",
            "Hammer Curls"
        ]

    # Exercise Choices for triceps
    elif muscle_choice == "4":
        muscle = "Triceps"
        exercises = [
            "Skull Crushers",
            "Dips",
            "Overhead Tricep Extension"
        ]

    # Applied Exercise choices for shoulders
    elif muscle_choice == "5":
        muscle = "Shoulders"
        exercises = [
            "Smith Machine Shoulder Press",
            "Shoulder Shrugs",
            "Upright Row"
        ]

    elif muscle_choice == "6":
        muscle = "Legs"

        # Step 3: Leg sub-groups
        print("\nSelect leg focus:")
        print("1. Quads")
        print("2. Hamstrings")
        print("3. Glutes")

        leg_choice = input("\nEnter 1–3: ")

        # Applied exercise choices for legs
        if leg_choice == "1":
            muscle = "Quads"
            exercises = [
                "Hack Squat",
                "Leg Extensions",
                "Bulgarian Squats"
            ]

        elif leg_choice == "2":
            muscle = "Hamstrings"
            exercises = [
                "Deadlift",
                "Lying Leg Curl",
                "Seated Leg Curl"
            ]

        elif leg_choice == "3":
            muscle = "Glutes"
            exercises = [
                "RDL (Romanian Deadlift)",
                "Hip Thrust",
                "Glute Kickback"
            ]

        else:
            print("Invalid leg choice.")
            exit()

    else:
        print("Invalid muscle choice.")
        exit()

    # Output
    print(f"\nGoal: {goal}")
    print(f"Muscle Group: {muscle}")

    print("\nWorkout Plan:")
    for ex in exercises:
        print(f"- {ex}: 2 sets to failure (increase weight on second set)")


# ---------------- LOSE WEIGHT ---------------- #
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


# ---------------- BODY RECOMP ---------------- #
elif goal_choice == "3":

    goal = "Body Recomp"

    print("\nSelect a muscle group:")
    print("1. Chest")
    print("2. Back")
    print("3. Biceps")
    print("4. Triceps")
    print("5. Shoulders")
    print("6. Legs")

    muscle_choice = input("\nEnter 1–6: ")

    # Chest
    if muscle_choice == "1":
        muscle = "Chest"
        workouts = [
            ("Barbell Bench Press", "4 sets x 6-8 reps"),
            ("Incline Dumbbell Press", "3 sets x 8-10 reps"),
            ("Cable or Pec Deck Flyes", "3 sets x 12-15 reps"),
            ("Push-Ups", "2 sets to failure")
        ]

    # Back
    elif muscle_choice == "2":
        muscle = "Back"
        workouts = [
            ("Deadlifts", "4 sets x 5 reps"),
            ("Pull-Ups or Lat Pulldowns", "4 sets x 8-10 reps"),
            ("Barbell Rows", "3 sets x 8-10 reps"),
            ("Seated Cable Rows", "3 sets x 10-12 reps"),
            ("Face Pulls", "3 sets x 12-15 reps")
        ]

    # Biceps
    elif muscle_choice == "3":
        muscle = "Biceps"
        workouts = [
            ("Barbell Curls", "3 sets x 8-10 reps"),
            ("Hammer Curls", "3 sets x 10-12 reps"),
            ("Preacher or Incline Dumbbell Curls", "2 sets x 12 reps")
        ]

    # Triceps
    elif muscle_choice == "4":
        muscle = "Triceps"
        workouts = [
            ("Tricep Pushdowns", "3 sets x 10-12 reps"),
            ("Overhead Dumbbell Tricep Extension", "3 sets x 10-12 reps"),
            ("Dips", "2 sets x 8-12 reps")
        ]

    # Shoulders
    elif muscle_choice == "5":
        muscle = "Shoulders"
        workouts = [
            ("Overhead Press", "4 sets x 6-8 reps"),
            ("Lateral Raises", "3 sets x 12-15 reps"),
            ("Rear Delt Flyes", "3 sets x 12-15 reps"),
            ("Front Raises", "2 sets x 12 reps")
        ]

    # Legs
    elif muscle_choice == "6":
        muscle = "Legs"
        workouts = [
            ("Barbell Squats", "4 sets x 6-8 reps"),
            ("Romanian Deadlifts", "3 sets x 8-10 reps"),
            ("Leg Press", "3 sets x 10-12 reps"),
            ("Walking Lunges", "2 sets x 12 steps each leg"),
            ("Leg Curls", "3 sets x 12 reps"),
            ("Calf Raises", "4 sets x 15 reps")
        ]

    else:
        print("Invalid muscle choice.")
        exit()

    # Output for body recomp
    print(f"\nGoal: {goal}")
    print(f"Muscle Group: {muscle}")

    print("\nWorkout Plan:")
    for ex, details in workouts:
        print(f"- {ex}: {details}")
# ---------------- DICTIONARY ---------------- #
elif goal_choice == "4":

    exercise_instructions = {
        "Pec Fly": "Keep a slight bend in your elbows, bring your arms together, squeeze your chest, then return slowly.",
        "Bench Press": "Lie flat, lower the bar to your chest, then press upward with control.",
        "Incline Press": "Set the bench on an incline, lower the weight to your upper chest, then press up.",
        "Dumbbell Incline Press": "Lower the dumbbells beside your upper chest, then press upward.",

        "Cable Pulldowns": "Pull the bar to your upper chest while keeping your chest up and squeezing your lats.",
        "Cable Rows": "Sit tall, pull the handle toward your stomach, squeeze your back, then return slowly.",
        "Single Arm Pulldown": "Pull one handle down toward your side and squeeze your lat.",

        "Incline Curls": "Sit on an incline bench, keep elbows still, curl the dumbbells, then lower slowly.",
        "Preacher Curls": "Keep your upper arms on the pad, curl the weight up, then lower with control.",
        "Hammer Curls": "Hold dumbbells with palms facing each other and curl without swinging.",

        "Skull Crushers": "Lower the weight toward your forehead while keeping elbows still, then extend your arms.",
        "Dips": "Lower your body by bending your elbows, then push back up using your triceps.",
        "Overhead Tricep Extension": "Lower the weight behind your head, then extend your arms upward.",

        "Smith Machine Shoulder Press": "Sit upright, lower the bar to chin level, then press overhead.",
        "Shoulder Shrugs": "Raise your shoulders straight up, squeeze, then lower slowly.",
        "Upright Row": "Pull the weight toward your chest while keeping it close to your body.",

        "Hack Squat": "Keep your back against the pad, lower with control, then push through your heels.",
        "Leg Extensions": "Extend your legs fully, squeeze your quads, then lower slowly.",
        "Bulgarian Squats": "Place one foot behind you, lower your body, then push through your front leg.",

        "Deadlift": "Keep your back flat, drive through your legs, and stand tall by extending your hips.",
        "Lying Leg Curl": "Curl your heels toward your glutes, squeeze your hamstrings, then lower slowly.",
        "Seated Leg Curl": "Curl the pad down using your hamstrings, pause, then return slowly.",

        "RDL (Romanian Deadlift)": "Keep knees slightly bent, hinge at your hips, lower the weight, then squeeze glutes to stand.",
        "Hip Thrust": "Place upper back on a bench, drive hips upward, squeeze glutes, then lower slowly.",
        "Glute Kickback": "Kick one leg back, squeeze your glute, and avoid arching your lower back.",

        "Diamond Push Ups": "Place hands in a diamond shape, lower your chest, then push back up.",
        "Plate on Back Push Ups": "Place a plate on your upper back and perform controlled push-ups.",
        "Slow Controlled Push Ups": "Lower slowly, pause near the bottom, then push back up.",
        "Side to Side Push Ups": "Shift your weight side to side while performing push-ups.",
        "Pike Push Ups": "Keep hips high, lower your head toward the floor, then press back up.",
        "Chair Dips": "Place hands on a chair, lower your body, then push up with your triceps.",

        "Bulgarian Leg Squats": "Place one foot behind you, lower on your front leg, then push back up.",
        "Single Leg Toe Touches": "Balance on one leg, hinge forward, touch toward your toes, then stand.",
        "Standing Calf Raises": "Rise onto your toes, squeeze calves, then lower slowly.",
        "Reverse Step Lunges": "Step backward into a lunge, lower your knee, then return to standing.",
        "Glute Bridges": "Lie on your back, drive hips upward, squeeze glutes, then lower.",

        "Chin Ups": "Grip the bar with palms facing you, pull your chin above the bar, then lower slowly.",
        "Pull Ups": "Grip palms away, pull your chest toward the bar, then lower with control.",
        "Inverted Barbell Row": "Lie under a bar, pull your chest to the bar, then lower slowly.",
        "Inverted Bicep Curl": "Hold a low bar with palms facing you and curl your body upward.",
        "Close Grip Pull Up": "Use a close grip, pull yourself upward, then lower slowly.",

        "Planks": "Keep your body straight, brace your core, and hold the position.",
        "Toe Touches": "Lie on your back, reach toward your toes, squeeze your abs, then lower.",
        "Russian Twists": "Sit back slightly and rotate side to side while keeping your core tight.",
        "Bicycle Crunches": "Bring opposite elbow to opposite knee in a controlled pedaling motion.",

        "Barbell Bench Press": "Lower the bar to your mid-chest, then press upward with control.",
        "Incline Dumbbell Press": "Lower dumbbells beside your upper chest, then press upward.",
        "Cable or Pec Deck Flyes": "Bring your arms together and squeeze your chest.",
        "Push-Ups": "Keep your body straight, lower your chest, then push back up.",

        "Deadlifts": "Keep your back flat, drive through your legs, and stand tall.",
        "Pull-Ups or Lat Pulldowns": "Pull your chest toward the bar or pull the cable bar to your upper chest.",
        "Barbell Rows": "Hinge forward, pull the bar toward your lower ribs, then lower slowly.",
        "Seated Cable Rows": "Pull the handle toward your stomach and squeeze your shoulder blades.",
        "Face Pulls": "Pull the rope toward your face with elbows high.",

        "Barbell Curls": "Keep elbows close, curl the bar upward, then lower slowly.",
        "Preacher or Incline Dumbbell Curls": "Keep upper arms stable and curl without swinging.",
        "Tricep Pushdowns": "Keep elbows at your sides and push the cable down until arms are straight.",
        "Overhead Dumbbell Tricep Extension": "Lower the dumbbell behind your head, then extend upward.",

        "Overhead Press": "Press the weight overhead while keeping your core tight.",
        "Lateral Raises": "Raise dumbbells to shoulder height, then lower slowly.",
        "Rear Delt Flyes": "Lean forward and raise weights out to the sides.",
        "Front Raises": "Raise weights in front of you to shoulder height.",

        "Barbell Squats": "Keep chest up, squat down with control, then push through your heels.",
        "Romanian Deadlifts": "Hinge at your hips, lower the weight, then squeeze glutes to stand.",
        "Leg Press": "Lower the platform slowly, then push through your heels.",
        "Walking Lunges": "Step forward into a lunge, then push through your front foot.",
        "Leg Curls": "Curl your heels toward your glutes, then lower slowly.",
        "Calf Raises": "Rise onto your toes, squeeze calves, then lower slowly."
    }

    print("\nExercise Dictionary:")
    exercise_list = list(exercise_instructions.keys())

    for i, exercise in enumerate(exercise_list, start=1):
        print(f"{i}. {exercise}")

    choice = input("\nChoose an exercise number: ")

    if choice.isdigit() and 1 <= int(choice) <= len(exercise_list):
        selected_exercise = exercise_list[int(choice) - 1]

        print("\nExercise Instructions")
        print("---------------------")
        print(f"Exercise: {selected_exercise}")
        print(f"How to do it: {exercise_instructions[selected_exercise]}")
    else:
        print("Invalid exercise choice.")