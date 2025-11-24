import os

import requests
import streamlit as st

API_URL = os.getenv("API_URL", "http://localhost:8000")

st.set_page_config(page_title="Agentic AI Tutor", layout="centered")
st.title("Agentic AI Tutor")

student_id = st.text_input("Student ID", value="demo-student")
subject_input = st.text_input("Subject (optional)", value="")
topic_input = st.text_input("Specific topic (optional)", value="")
question = st.text_input("What topic are you struggling with?")


def show_error(resp: requests.Response) -> None:
    st.error(f"Request failed ({resp.status_code}): {resp.text}")


if st.button("Ask Tutor"):
    payload = {"question": question, "student_id": student_id}
    if subject_input.strip():
        payload["subject"] = subject_input.strip()
    if topic_input.strip():
        payload["topic"] = topic_input.strip()

    resp = requests.post(
        f"{API_URL}/ask/",
        json=payload,
        timeout=30,
    )
    if resp.ok:
        data = resp.json()
        st.success(data["natural_language_response"])
        st.write("**Plan executed**")
        st.write("\n".join(f"• {step}" for step in data["plan_executed"]))
        st.info(data["retrieved_content"])
        st.write("**Quiz suggestions**")
        st.table(data["quiz"])
        st.caption("Raw response")
        st.json(data)
    else:
        show_error(resp)

st.subheader("Request Quiz")
quiz_topic = st.text_input("Quiz topic", value="Probability")
quiz_subject = st.text_input("Quiz subject (optional)", value="")
difficulty = st.selectbox("Difficulty", ["easy", "medium", "hard"], index=1)
num_questions = st.slider("Number of questions", 1, 10, 3)

if st.button("Generate Quiz"):
    payload = {
        "topic": quiz_topic,
        "difficulty": difficulty,
        "num_questions": num_questions,
        "student_id": student_id,
    }
    if quiz_subject.strip():
        payload["subject"] = quiz_subject.strip()

    resp = requests.post(
        f"{API_URL}/quiz/",
        json=payload,
        timeout=30,
    )
    if resp.ok:
        data = resp.json()
        st.write(f"{data['topic']} quiz ({data['difficulty']})")
        st.table(data["questions"])
        st.caption("Raw response")
        st.json(data)
    else:
        show_error(resp)

if st.button("View Progress"):
    resp = requests.get(f"{API_URL}/progress/{student_id}", timeout=30)
    if resp.ok:
        data = resp.json()
        st.write("**Agent recommendation**")
        st.success(data["agent_recommendation"])
        st.write(data["natural_language_summary"])
        table_rows = [
            {"topic": topic_name, **metrics}
            for topic_name, metrics in data["progress"].items()
        ]
        st.table(table_rows)
        st.caption("Raw response")
        st.json(data)
    else:
        show_error(resp)

