# GenAI Project Reviewer & Improver

##  Overview
GenAI Project Reviewer is a **Generative AI–powered application** that evaluates AI/ML project descriptions and provides **structured, actionable feedback**.  
It helps students understand the strengths, weaknesses, and improvement areas of their projects and also generates **resume-ready bullet points**.

The system is designed to mimic how a **senior AI engineer or recruiter** reviews technical projects.

---

##  Problem Statement
Students often build AI/ML projects but lack:
- Structured technical feedback  
- Clarity on real-world relevance  
- Guidance on how to present projects on resumes or in interviews  

Manual reviews are inconsistent and not easily scalable.

---

##  Solution
This project uses a **Large Language Model (LLM)** to:
- Analyze project descriptions
- Evaluate technical depth and innovation
- Suggest concrete improvements
- Generate resume-friendly bullet points

The system enforces **structured outputs** through prompt engineering, making the feedback consistent and repeatable.

---

##  Key Features
- Evaluates AI/ML projects across multiple dimensions
- Provides strengths and weaknesses clearly
- Suggests actionable improvements
- Generates resume-ready bullet points
- Supports **conversational interaction** with memory
- Lightweight and easy to extend

---

##  Tech Stack
- **Python**
- **Streamlit** – Web interface
- **Groq API** – LLaMA-3.1 LLM (open-source)
- **Prompt Engineering**
- **Session-based conversational memory**

---

##  How It Works
1. User enters a project description or follow-up query
2. System constructs a structured prompt
3. Prompt is sent to an LLM via Groq API
4. Model generates structured feedback
5. Output is displayed in an interactive web interface
6. Conversation context is preserved across turns

---

## How to Run the Project

### 1. Install dependencies
```bash
pip install streamlit groq
```
### 2. Set environmental variable 
```bash
GROQ_API_KEY=your_api_key_here
```
### 3. Run the application
```bash
streamlit run app.py
```
![App Screenshot](screenshot(97).png)

