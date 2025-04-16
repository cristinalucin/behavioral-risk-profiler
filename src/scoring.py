from survey_questions import SURVEY_QUESTIONS, LIKERT_SCORES
from collections import defaultdict

def calculate_risk_score(responses):
    """
    Calculate overall and category-based risk scores.

    Parameters:
        responses (dict): {question_id: selected_answer}

    Returns:
        dict: Total and per-category risk scores, normalized to 0-100 scale
    """
    category_scores = defaultdict(list)
    total_score = 0

    for q in SURVEY_QUESTIONS:
        qid = q["id"]
        selected_answer = responses.get(qid)

        if selected_answer in ["Yes", "No"]:
            # Handle Yes/No questions
            score = 1 if selected_answer == "Yes" else 0
        elif selected_answer in LIKERT_SCORES:
            # Handle Likert-scale questions
            score = LIKERT_SCORES[selected_answer]
        else:
            continue  # Skip unanswered or invalid responses

        category = q["category"]
        category_scores[category].append(score)
        total_score += score

    # Normalize scores (if needed)
    return {
        "total_score": total_score,
        "category_scores": {
            cat: sum(scores) for cat, scores in category_scores.items()
        }
    }

def flag_high_risk_areas(score_dict, threshold=70):
    """
    Identify risk categories exceeding a threshold.

    Parameters:
        score_dict (dict): Output of calculate_risk_score()
        threshold (int): Risk score threshold (0-100)

    Returns:
        list of high-risk categories
    """
    return [cat for cat, score in score_dict["category_scores"].items() if score >= threshold]

def is_overall_high_risk(total_score, threshold=70):
    """
    Determine if the overall score exceeds the high-risk threshold.

    Parameters:
        total_score (float): Total normalized risk score (0-100)
        threshold (int): Risk score threshold (default: 70)

    Returns:
        bool: True if total score exceeds threshold, False otherwise
    """
    return total_score >= threshold
