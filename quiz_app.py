import json
import os

print("=" * 40)
print("       WELCOME TO THE QUIZ APP")
print("=" * 40)

def get_valid_answer():
    answer = input("Enter your answer (A/B/C/D): ").strip().upper()

    while answer not in ["A", "B", "C", "D"]:
        print("Invalid input! Please enter A, B, C, or D.")
        answer = input("Enter your answer (A/B/C/D): ").strip().upper()

    return answer

print("Test your knowledge with this quiz!")
print("There will be 5 questions. Good luck!")


def choose_difficulty():
    print("\nChoose your difficulty level:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")

    choice = input("Enter your choice (1/2/3): ").strip()

    while choice not in ["1", "2", "3"]:
        print("Invalid choice! Please enter 1, 2, or 3.")
        choice = input("Enter your choice (1/2/3): ").strip()

    if choice == "1":
        return "Easy"
    elif choice == "2":
        return "Medium"
    else:
        return "Hard"


questions = [
    {
        "question": "What is the capital of India?",
        "options": ["A. Mumbai", "B. New Delhi", "C. Chandigarh", "D. Kolkata"],
        "answer": "B"
    },
    {
        "question": "Which programming language are we using?",
        "options": ["A. Java", "B. C++", "C. Python", "D. JavaScript"],
        "answer": "C"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Jupiter", "C. Mars", "D. Venus"],
        "answer": "C"
    },
    {
        "question": "What does CPU stand for?",
        "options": [
            "A. Central Processing Unit",
            "B. Computer Personal Unit",
            "C. Central Program Utility",
            "D. Control Processing User"
        ],
        "answer": "A"
    },
    {
        "question": "Which Python data structure stores key-value pairs?",
        "options": ["A. List", "B. Tuple", "C. Dictionary", "D. Set"],
        "answer": "C"
    }
]

medium_questions = [
    {
        "question": "What is the time complexity of binary search?",
        "options": ["A. O(n)", "B. O(log n)", "C. O(n²)", "D. O(1)"],
        "answer": "B"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["A. function", "B. define", "C. def", "D. fun"],
        "answer": "C"
    },
    {
        "question": "Which data structure follows FIFO?",
        "options": ["A. Stack", "B. Queue", "C. Tree", "D. Graph"],
        "answer": "B"
    },
    {
        "question": "What does len([10, 20, 30]) return?",
        "options": ["A. 2", "B. 10", "C. 3", "D. 30"],
        "answer": "C"
    },
    {
        "question": "Which method adds an item to the end of a list?",
        "options": ["A. add()", "B. append()", "C. insert_end()", "D. push()"],
        "answer": "B"
    }
]

hard_questions = [
    {
        "question": "Which Python feature allows a function to call itself?",
        "options": ["A. Iteration", "B. Recursion", "C. Inheritance", "D. Importing"],
        "answer": "B"
    },
    {
        "question": "Which data structure is commonly used in BFS?",
        "options": ["A. Stack", "B. Queue", "C. Heap", "D. Set"],
        "answer": "B"
    },
    {
        "question": "What is the average time complexity of dictionary lookup in Python?",
        "options": ["A. O(n)", "B. O(log n)", "C. O(1)", "D. O(n²)"],
        "answer": "C"
    },
    {
        "question": "Which Python structure is immutable?",
        "options": ["A. List", "B. Dictionary", "C. Set", "D. Tuple"],
        "answer": "D"
    },
    {
        "question": "Which algorithmic technique solves problems by breaking them into overlapping subproblems?",
        "options": ["A. Greedy", "B. Dynamic programming", "C. Linear search", "D. Bubble sort"],
        "answer": "B"
    }
]

def save_result(player_name, score, difficulty):
    result = {
        "name": player_name,
        "score": score,
        "difficulty": difficulty
    }

    if os.path.exists("leaderboard.json"):
        with open("leaderboard.json", "r") as file:
            leaderboard = json.load(file)
    else:
        leaderboard = []

    leaderboard.append(result)

    with open("leaderboard.json", "w") as file:
        json.dump(leaderboard, file, indent=4)

    print("Your result has been saved successfully!")

def show_leaderboard():
    print("\n" + "=" * 40)
    print("             LEADERBOARD")
    print("=" * 40)

    if not os.path.exists("leaderboard.json"):
        print("No results available yet!")
        return

    with open("leaderboard.json", "r") as file:
        leaderboard = json.load(file)

    if not leaderboard:
        print("No results available yet!")
        return

    best_scores = {}

    for result in leaderboard:
        name_key = result["name"].strip().casefold()

        if (
            name_key not in best_scores
            or result["score"] > best_scores[name_key]["score"]
        ):
            best_scores[name_key] = result

    sorted_scores = sorted(
        best_scores.values(),
        key=lambda result: result["score"],
        reverse=True
    )

    for rank, result in enumerate(sorted_scores, start=1):
        print(
            f"{rank}. {result['name']} | "
            f"Best Score: {result['score']}/5 | "
            f"Difficulty: {result['difficulty']}"
        )

    print("=" * 40)


def show_statistics():
    print("\n" + "=" * 40)
    print("            QUIZ STATISTICS")
    print("=" * 40)

    if not os.path.exists("leaderboard.json"):
        print("No quiz data available yet!")
        return

    with open("leaderboard.json", "r") as file:
        leaderboard = json.load(file)

    if not leaderboard:
        print("No quiz data available yet!")
        return

    total_attempts = len(leaderboard)
    scores = [result["score"] for result in leaderboard]

    average_score = sum(scores) / total_attempts
    highest_score = max(scores)
    perfect_scores = scores.count(5)

    print("Total attempts:", total_attempts)
    print(f"Average score: {average_score:.2f}/5")
    print("Highest score:", highest_score, "/ 5")
    print("Perfect scores:", perfect_scores)

    print("=" * 40)


def show_instructions():
    print("\n" + "=" * 40)
    print("             HOW TO PLAY")
    print("=" * 40)

    print("1. Choose a difficulty: Easy, Medium, or Hard.")
    print("2. Enter your name before starting.")
    print("3. Each quiz contains 5 questions.")
    print("4. Select your answer using A, B, C, or D.")
    print("5. Each correct answer earns 1 point.")
    print("6. Incorrect answers show the correct option.")
    print("7. Your final score and percentage appear at the end.")
    print("8. Your result is saved to the leaderboard.")
    print("9. You can view the leaderboard and statistics")
    print("   from the main menu.")

    print("=" * 40)


def play_quiz():
    score = 0
    wrong_answers = []
    difficulty = choose_difficulty()
    player_name = input("Enter your name: ").strip()

    while not player_name:
        print("Name cannot be empty!")
        player_name = input("Enter your name: ").strip()
        
    print("\nYou selected:", difficulty)
    
    if difficulty == "Easy":
        selected_questions = questions
    elif difficulty == "Medium":
        selected_questions = medium_questions
    else:
        selected_questions = hard_questions

    for question in selected_questions:
        print("\n" + question["question"])

        for option in question["options"]:
            print(option)

        answer = get_valid_answer()

        if answer == question["answer"]:
            print("Correct! 🎉")
            score += 1
        else:
            print("Incorrect! ❌")
            wrong_answers.append(question)

            correct_answer = question["answer"]

            for option in question["options"]:
                if option.startswith(correct_answer + "."):
                    print("Correct answer:", option)
                    break

        print("Your current score is:", score)

    print("\n" + "=" * 40)
    print("           QUIZ COMPLETED!")
    print("=" * 40)

    print("Your final score:", score, "/", len(selected_questions))
    percentage = (score / len(selected_questions)) * 100
    print("Your percentage:", percentage, "%")

    if percentage == 100:
        print("Excellent! Perfect score! 🏆")
    elif percentage >= 60:
        print("Great job! Keep it up! 🎉")
    elif percentage >= 40:
        print("Good effort! Keep practicing! 💪")
    else:
        print("Don't give up! Practice makes perfect. 😊")

    print("=" * 40)

    save_result(player_name, score, difficulty)
    show_leaderboard()
    
    if wrong_answers:
        print("\nQuestions to review:")

        for question in wrong_answers:
            print("-", question["question"])

            correct_answer = question["answer"]

            for option in question["options"]:
                if option.startswith(correct_answer + "."):
                    print("  Correct answer:", option)
                    break
    else:
        print("\nPerfect! You answered every question correctly! 🎉")


def main_menu():
    while True:
        print("\n" + "=" * 40)
        print("          PYTHON QUIZ APP")
        print("=" * 40)
        print("1. Start Quiz")
        print("2. View Leaderboard")
        print("3. View Statistics")
        print("4. How to Play")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4/5): ").strip()

        if choice == "1":
            play_quiz()

        elif choice == "2":
            show_leaderboard()

        elif choice == "3":
            show_statistics()

        elif choice == "4":
            show_instructions()

        elif choice == "5":
            print("Thanks for playing! Goodbye! 👋")
            break

        else:
            print("Invalid choice! Please enter 1, 2, 3, 4, or 5.")

main_menu()