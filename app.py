import streamlit as st
import os
from groq import Groq

# Initialize Groq client
client = Groq(api_key=os.getenv("GROQ_GENAI_API"))

BASE_PROMPT = """
You are a senior AI engineer reviewing a student AI/ML project.

Evaluate the project on:
1. Technical depth
2. Innovation
3. Real-world applicability
4. Resume impact

Provide output in this EXACT format:

Quality Level: (Low / Medium / High)

Strengths:
- Point 1
- Point 2

Weaknesses:
- Point 1
- Point 2

Improvement Suggestions:
- Suggestion 1
- Suggestion 2

Resume Bullet Points:
- Bullet 1
- Bullet 2
"""

def review_project(project_text):
    prompt = BASE_PROMPT + "\n\nProject Description:\n" + project_text

    response = client.chat.completions.create(
        model="llama-3.1-70b-versatile",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )

    return response.choices[0].message.content


st.title("GenAI Project Reviewer (Free LLaMA-3)")

project_text = st.text_area(
    "Paste your project description here",
    height=200
)

if st.button("Review Project"):
    if project_text.strip() == "":
        st.warning("Please enter a project description.")
    else:
        with st.spinner("Reviewing project..."):
            result = review_project(project_text)
            st.subheader("AI Review")
            st.write(result)




