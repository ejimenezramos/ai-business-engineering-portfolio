# 🧠 AI Requirements Analyzer

Live demo:
https://ai-business-requirements-analysis.streamlit.app/

AI-powered tool that translates business requirements into structured technical tasks, effort estimation and risk analysis.

Designed for business-oriented technical roles, consultants and engineers working at the intersection of technology and real-world problem solving.

---

## 🚀 What problem does this solve?

In many projects, requirements are written in natural language and contain ambiguities, missing details or hidden technical risks.

This tool helps to:
- Bridge the gap between business language and technical execution
- Identify missing information early
- Support better estimations and technical decision-making

---

## ✨ Features

- 🔍 Analyze raw business requirements using Generative AI (Gemini)
- 🛠 Extract concrete technical tasks
- ⏱ Provide rough effort estimation
- ⚠️ Highlight risks and ambiguities
- 🧩 Clean, professional UI built with Streamlit

---

## 🖥️ User Interface

### Home
![Home](screenshots/01_home.png)

### Technical Tasks
![Technical Tasks](screenshots/03_technical_tasks.png)

### Estimation
![Estimation](screenshots/04_estimation.png)

### Risks & Ambiguities
![Risks](screenshots/05_risks.png)

---

## 🧠 Tech Stack

- Python
- Streamlit (UI)
- Google Gemini API (Generative AI)
- Modular architecture (AI logic separated from UI)

---

## 🏗️ Architecture Overview

requirements_analysis_ai/
├── app/              # Core application logic
├── ui/               # Streamlit UI
├── ai_service.py     # Gemini integration & prompt logic
├── screenshots/      # UI screenshots
└── README.md

---

## 🔐 Configuration

Set your Gemini API key as an environment variable.

macOS / Linux:
export GEMINI_API_KEY=your_api_key_here

Windows (PowerShell):
setx GEMINI_API_KEY "your_api_key_here"

---

## ▶️ Run locally

pip install -r requirements.txt
streamlit run ui/app.py

---

## 📌 Why this project?

This project reflects my interest in roles where:
- Understanding the business context is as important as coding
- Technology must work in real enterprise environments
- AI is used as a productivity and decision-support tool, not as a gimmick

---

## 🎯 Target Roles

- Solutions Engineer
- Technical Consultant
- Business-focused Software Engineer
- AI Engineer (applied / product-oriented)
- Product or Platform Engineering roles

---

## 📄 License

MIT
