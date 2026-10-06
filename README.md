# Python Quiz Application

A quiz application built using Python, featuring both a command-line version and an interactive web version built with Streamlit.

## Features

### Command-Line Version

- Three difficulty levels: Easy, Medium, and Hard
- Multiple-choice questions
- Input validation
- Score and percentage calculation
- Feedback based on performance
- Review of incorrect answers
- JSON-based leaderboard
- Quiz statistics
- How to Play instructions
- Main menu for navigation

### Web Version

- Interactive web interface using Streamlit
- Player name validation
- Three difficulty levels: Easy, Medium, and Hard
- Multiple-choice questions
- Instant answer feedback
- Progress bar
- Answer locking after submission
- Final score and percentage
- Performance-based feedback
- JSON-based leaderboard
- Best score tracking for each player
- How to Play section
- Play Again option
- Back to Home option

## 📸 Screenshots

### Command-Line Version

![Python Quiz Output](screenshots/python-quiz.png)

![Python Quiz Leaderboard](screenshots/quiz-leaderboard.png)

![Python Quiz Statistics](screenshots/quiz-statistics.png)

### Web Version

_Streamlit screenshots will be added after deployment._

## Technologies Used

- Python
- Streamlit
- JSON
- File handling
- Session State
- Functions
- Loops
- Lists
- Dictionaries

## How to Run

### Command-Line Version

1. Install Python.
2. Open the project folder in VS Code.
3. Run the following command in the terminal:

```bash
python quiz_app.py
```

### Web Version

1. Install Streamlit:

```bash
pip install streamlit
```

2. Run the Streamlit application:

```bash
streamlit run quiz_web.py
```

3. The application will open in your browser.

## Data Storage

Quiz results are saved locally in `leaderboard.json`.

The leaderboard keeps track of players' best scores. The `leaderboard.json` file is excluded from Git using `.gitignore`.

## Project Structure

```text
Python-Quiz-Application/
│
├── quiz_app.py
├── quiz_web.py
├── README.md
├── .gitignore
│
└── screenshots/
    ├── python-quiz.png
    ├── quiz-leaderboard.png
    └── quiz-statistics.png
```

## Future Improvements

- Add more questions
- Add more difficulty levels
- Add a timer for the web version
- Add more detailed quiz analytics
- Deploy the Streamlit application online