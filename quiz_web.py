import streamlit as st
import json

if "question_index" not in st.session_state:
    st.session_state.question_index = 0

if "score" not in st.session_state:
    st.session_state.score = 0

if "answered" not in st.session_state:
    st.session_state.answered = False

if "feedback" not in st.session_state:
    st.session_state.feedback = ""

if "quiz_started" not in st.session_state:
    st.session_state.quiz_started = False

if "result_saved" not in st.session_state:
    st.session_state.result_saved = False

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

    try:
        with open("leaderboard.json", "r") as file:
            leaderboard = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        leaderboard = []

    leaderboard.append(result)

    with open("leaderboard.json", "w") as file:
        json.dump(leaderboard, file, indent=4)

def get_leaderboard():
    try:
        with open("leaderboard.json", "r") as file:
            leaderboard = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

    if not leaderboard:
        return []

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

    return sorted_scores

st.title("🎯 Python Quiz Application")

st.write("Welcome to the Quiz Application!")

name = st.text_input("Enter your name:")

if name:
    st.write(f"Hello, {name}! 👋")

difficulty = st.selectbox(
    "Choose difficulty:",
    ["Easy", "Medium", "Hard"]
)

if "last_difficulty" not in st.session_state:
    st.session_state.last_difficulty = difficulty

if st.session_state.last_difficulty != difficulty:
    st.session_state.question_index = 0
    st.session_state.score = 0
    st.session_state.answered = False
    st.session_state.last_difficulty = difficulty
    st.session_state.feedback = ""

st.write(f"You selected: **{difficulty}**")

if st.button("Start Quiz"):
     if not name.strip():
        st.warning("Please enter your name before starting the quiz.")

     else:
        st.session_state.question_index = 0
        st.session_state.score = 0
        st.session_state.answered = False
        st.session_state.feedback = ""
        st.session_state.result_saved = False
        st.session_state.quiz_started = True
        st.rerun()

with st.expander("🏆 View Leaderboard"):

    leaderboard = get_leaderboard()

    if not leaderboard:
        st.info("No results available yet!")

    else:
        for rank, result in enumerate(leaderboard, start=1):
            st.write(
                f"**{rank}. {result['name']}** — "
                f"{result['score']}/5 — "
                f"{result['difficulty']}"
            )

with st.expander("📖 How to Play"):

    st.write("• Enter your name before starting the quiz.")
    st.write("• Choose a difficulty level: Easy, Medium, or Hard.")
    st.write("• The quiz contains 5 questions.")
    st.write("• Select one answer for each question.")
    st.write("• Click Submit Answer to check your answer.")
    st.write("• Your final score will be shown at the end.")
    st.write("• Your result will be saved to the leaderboard.")

st.divider()

# Select the question set based on difficulty
if difficulty == "Easy":
    selected_questions = questions
elif difficulty == "Medium":
    selected_questions = medium_questions
else:
    selected_questions = hard_questions


# Show quiz only after clicking Start Quiz
if st.session_state.quiz_started:

    current_question = selected_questions[st.session_state.question_index]

    st.subheader(
        f"Question {st.session_state.question_index + 1} "
        f"of {len(selected_questions)}"
    )

    if st.session_state.answered and (
        st.session_state.question_index == len(selected_questions) - 1
):
        progress = 1.0
    else:
        progress = (
            st.session_state.question_index
            / len(selected_questions)
            )

    st.progress(progress)

    st.markdown(
        f"### {current_question['question']}"
    )

    answer = st.radio(
        "Choose your answer:",
        current_question["options"],
        disabled=st.session_state.answered
        )

    if not st.session_state.answered:

        if st.button("Submit Answer"):

            selected_letter = answer.split(".")[0]

            if selected_letter == current_question["answer"]:
                st.session_state.score += 1
                st.session_state.feedback = "Correct! 🎉"
            else:
                st.session_state.feedback = (
                    f"Incorrect! ❌ Correct answer: "
                    f"{current_question['answer']}"
                )

            st.session_state.answered = True
            st.rerun()

    # Display feedback after submission
    if st.session_state.answered:

        if st.session_state.feedback.startswith("Correct"):
            st.success(st.session_state.feedback)
        else:
            st.error(st.session_state.feedback)

        if st.session_state.question_index < len(selected_questions) - 1:

            if st.button("Next Question"):
                st.session_state.question_index += 1
                st.session_state.answered = False
                st.session_state.feedback = ""
                st.rerun()

        else:
            st.success("Quiz completed! 🎉")

            score = st.session_state.score
            total = len(selected_questions)

            percentage = (score / total) * 100

            if not st.session_state.result_saved:
                save_result(name, score, difficulty)
                st.session_state.result_saved = True

            save_result(name, score, difficulty)

            st.subheader("🏆 Your Final Result")

            col1, col2 = st.columns(2)

            with col1:
                st.metric("Score", f"{score}/{total}")

            with col2:
                st.metric("Percentage", f"{percentage:.1f}%")

            if percentage == 100:
                st.balloons()
                st.success("Excellent! Perfect score! 🌟")

            elif percentage >= 80:
                st.success("Great job! 🎉")

            elif percentage >= 60:
                st.info("Good work! Keep practicing. 👍")

            elif percentage >= 40:
                st.warning("Not bad! A little more practice will help. 💪")

            else:
                st.error("Keep practicing! You can improve. 📚")

            if st.button("Play Again"):
                st.session_state.question_index = 0
                st.session_state.score = 0
                st.session_state.answered = False
                st.session_state.feedback = ""
                st.rerun()

            if st.button("🏠 Back to Home"):
                st.session_state.quiz_started = False
                st.session_state.question_index = 0
                st.session_state.score = 0
                st.session_state.answered = False
                st.session_state.feedback = ""
                st.session_state.result_saved = False
                st.rerun()