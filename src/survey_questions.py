import random

# Likelihood-based answers
LIKERT_LIKELIHOOD = [
    "Very likely",         # 3 points (highest risk)
    "Somewhat likely",     # 2 points
    "Somewhat unlikely",   # 1 point
    "Very unlikely"        # 0 points (lowest risk)
]

# Frequency-based answers
LIKERT_FREQUENCY = [
    "Always",              # 3 points (highest risk)
    "Often",               # 2 points
    "Rarely",              # 1 point
    "Never"                # 0 points (lowest risk)
]

# Agreement-based answers
LIKERT_AGREEMENT = [
    "Strongly agree",      # 3 points (highest risk)
    "Agree",               # 2 points
    "Disagree",            # 1 point
    "Strongly disagree"    # 0 points (lowest risk)
]

# Confidence-based answers
LIKERT_CONFIDENCE = [
    "Very confident",      # 0 points (lowest risk)
    "Somewhat confident",  # 1 point
    "Not very confident",  # 2 points
    "Not confident at all" # 3 points (highest risk)
]

# Mapping each answer to a numeric risk score (index-based)
LIKERT_SCORES = {
    # Likelihood-based answers
    "Very likely": 3,
    "Somewhat likely": 2,
    "Somewhat unlikely": 1,
    "Very unlikely": 0,

    # Frequency-based answers
    "Always": 3,
    "Often": 2,
    "Rarely": 1,
    "Never": 0,

    # Agreement-based answers
    "Strongly agree": 3,
    "Agree": 2,
    "Disagree": 1,
    "Strongly disagree": 0,

    # Confidence-based answers
    "Very confident": 0,
    "Somewhat confident": 1,
    "Not very confident": 2,
    "Not confident at all": 3
}

# Questions grouped by fraud triangle category
SURVEY_QUESTIONS = [
    # --- Pressure ---
    {
        "id": 1,
        "text": "How often do you experience personal financial stress that affects your focus or well-being at work?",
        "category": "pressure",
        "options": LIKERT_FREQUENCY  # Always, Often, Rarely, Never
    },
    {
        "id": 2,
        "text": "How often do you rely on credit cards or loans to cover everyday expenses?",
        "category": "pressure",
        "options": LIKERT_FREQUENCY
    },
    {
        "id": 3,
        "text": "In previous roles, I have felt that my compensation was not aligned with my responsibilities or contributions.",
        "category": "pressure",
        "options": LIKERT_AGREEMENT  # Strongly agree, Agree, Disagree, Strongly disagree
    },
    {
        "id": 4,
        "text": "If you encountered a sudden $1,000 emergency today, how confident are you in handling it without external help?",
        "category": "pressure",
        "options": LIKERT_CONFIDENCE
    },
    {
        "id": 5,
        "text": "I believe that long-term loyalty to a company should entitle employees to occasional, unspoken perks.",
        "category": "pressure",
        "options": LIKERT_AGREEMENT
    },
    {
        "id": 6,
        "text": "Have you ever felt that your personal financial situation could impact your decision-making at work?",
        "category": "pressure",
        "options": ["Yes", "No"]  # Yes/No question
    },

    # --- Opportunity ---
    {
        "id": 7,
        "text": "How comfortable are you allowing coworkers to access or check your work?",
        "category": "opportunity",
        "options": LIKERT_CONFIDENCE
    },
    {
        "id": 8,
        "text": "How confident are you in handling sensitive processes (e.g., financial records, payroll, data) without oversight?",
        "category": "opportunity",
        "options": LIKERT_CONFIDENCE  # Very confident, Somewhat confident, Not very confident, Not confident at all
    },
    {
        "id": 9,
        "text": "How often do you delay implementing a control or audit step because it slows you down?",
        "category": "opportunity",
        "options": LIKERT_FREQUENCY  # Always, Often, Rarely, Never
    },

    # --- Rationalization ---
    {
        "id": 10,
        "text": "I think it is acceptable to bend minor rules if it benefits the company.",
        "category": "rationalization",
        "options": LIKERT_AGREEMENT  # Strongly agree, Agree, Disagree, Strongly disagree
    },
    {
        "id": 11,
        "text": "How often have you thought, 'No one would notice' while completing a sensitive work task?",
        "category": "rationalization",
        "options": LIKERT_FREQUENCY  # Always, Often, Rarely, Never
    },
    {
        "id": 12,
        "text": "If you felt that a policy was unfair or unnecessary, how likely would you be to follow it anyway?",
        "category": "rationalization",
        "options": LIKERT_LIKELIHOOD
    },
    {
        "id": 13,
        "text": "Employees should sometimes be trusted more than policies or rules.",
        "category": "rationalization",
        "options": LIKERT_AGREEMENT  # Strongly agree, Agree, Disagree, Strongly disagree
    },
    {
        "id": 14,
        "text": "I believe employees' judgment should sometimes take precedence over company policies or rules.",
        "category": "rationalization",
        "options": LIKERT_AGREEMENT  # Strongly agree, Agree, Disagree, Strongly disagree
    },

    # --- Behavioral Risk Indicators ---
    {
        "id": 15,
        "text": "How often do you feel frustrated by company rules or procedures?",
        "category": "behavioral",
        "options": LIKERT_FREQUENCY
    },
    {
        "id": 16,
        "text": "Have you ever been warned, disciplined, or investigated for any work behavior?",
        "category": "behavioral",
        "options": ["Yes", "No"]  # Yes/No question
    },
    {
        "id": 17,
        "text": "How often do you share login credentials or badge access with others (even for convenience)?",
        "category": "behavioral",
        "options": LIKERT_FREQUENCY
    },
    {
        "id": 18,
        "text": "How likely are you to reflect on feedback or warnings about your work behavior?",
        "category": "behavioral",
        "options": LIKERT_LIKELIHOOD  # Very likely, Somewhat likely, Somewhat unlikely, Very unlikely
    }
]

def get_randomized_questions():
    """
    Returns a randomized list of survey questions.
    """
    randomized_questions = SURVEY_QUESTIONS[:]
    random.shuffle(randomized_questions)
    return randomized_questions
