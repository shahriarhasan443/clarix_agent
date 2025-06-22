# Clarix Agent

# Clarix Agent (ADK Multi-Agent System)

Clarix is an AI-powered content generation assistant built using Google's Agent Development Kit (ADK). It coordinates multiple agents to help generate marketing content including target audience insights, ad copy, promotional emails, and tone-optimized messages.

---

## 💡 Features

- Multi-agent architecture using ADK
- Powered by Gemini 2.5 Flash model
- Input-driven content generation
- Designed for ADK Web/CLI execution
- Easily extensible

---

## 🗂️ Project Structure

clarix_agent/
├── agents/
│ ├── audience_agent.py
│ ├── ad_writer_agent.py
│ ├── email_writer_agent.py
│ └── tone_optimizer_agent.py
├── utils/
│ └── input_handler.py
├── agent.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md


---

## ⚙️ Setup Instructions

### 1. Create and activate virtual environment

```bash
python -m venv venv
.\venv\Scripts\activate

pip install -r requirements.txt

🚀 Run with ADK
Make sure you're in the root project directory, then run:
adk web
