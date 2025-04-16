# app/main.py

import sys
import os
import streamlit as st

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from survey_questions import get_randomized_questions
from scoring import calculate_risk_score, flag_high_risk_areas, is_overall_high_risk

st.set_page_config(page_title="Behavioral Risk Profiler", layout="wide")
st.title("🛡️ Behavioral Risk Profiler for Occupational Fraud")
st.markdown("This screening tool is designed to help identify potential behavioral red flags in high-risk hiring scenarios.")

# Store responses here
responses = {}

# Get randomized questions
questions = get_randomized_questions()

# Use the randomized questions in your survey form
with st.form("fraud_risk_form"):
    for question in questions:
        qid = question["id"]
        qtext = question["text"]
        category = question["category"].capitalize()

        selected = st.radio(
            f"**({category}) Q{qid}:** {qtext}",
            options=["-- Select an answer --"] + question["options"],
            key=f"q_{qid}"
        )

        responses[qid] = selected

    submitted = st.form_submit_button("Calculate Risk Score")

if submitted:
    # Check for unanswered questions
    unanswered = [qid for qid, answer in responses.items() if answer == "-- Select an answer --"]

    if unanswered:
        st.warning(f"⚠️ Please answer all questions before submitting. Unanswered: {len(unanswered)}")
    else:
        # Calculate risk scores
        score_result = calculate_risk_score(responses)
        total_score = score_result["total_score"]
        category_scores = score_result["category_scores"]
        high_risk_flags = flag_high_risk_areas(score_result)

        # Display results
        st.divider()
        st.subheader("📊 Results")
        st.metric("Total Risk Score", f"{total_score}/100")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("### 🔍 Category Breakdown")
            for category, score in category_scores.items():
                bar_color = "red" if score >= 70 else ("orange" if score >= 50 else "green")
                st.markdown(f"**{category.capitalize()}:**")
                st.progress(score / 100.0)
                st.caption(f"{score}/100")

        with col2:
            if high_risk_flags:
                st.markdown("### ⚠️ High-Risk Flags")
                st.error(f"High-risk categories: {', '.join(high_risk_flags)}")
            else:
                st.markdown("### ✅ No High-Risk Flags")
                st.success("No categories exceeded the high-risk threshold.")

        # Check overall high-risk status
        if is_overall_high_risk(total_score):
            st.error("🚨 Overall Risk Level: HIGH")
        else:
            st.success("✅ Overall Risk Level: LOW/MODERATE")
