# 🧠 Explain AI — ELI5 Web App

<p align="center">
  <b>Understand anything, at your level.</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python">
  <img src="https://img.shields.io/badge/Flask-Web%20Framework-black?logo=flask">
  <img src="https://img.shields.io/badge/Deployment-Render-purple?logo=render">
  <img src="https://img.shields.io/badge/API-OpenRouter-green">
</p>

---

## 🚀 Live Demo

👉 https://explain-ai-app-1.onrender.com

---

## ✨ What it does

Explain AI is a web app that takes any topic and explains it in **different difficulty levels** — from beginner to advanced.

Perfect for:

* 📚 Students
* 🧠 Quick revision
* 🤯 Simplifying complex topics

---

## 🎯 Features

* 📝 Enter any topic
* 🎚 Select difficulty level
* ⚡ Instant AI-generated explanation
* 🌐 Fully deployed web app
* 🔐 Secure API key handling (env variables)

---

## 🛠 Tech Stack

| Layer      | Technology     |
| ---------- | -------------- |
| Backend    | Flask (Python) |
| Frontend   | HTML, CSS      |
| AI API     | OpenRouter     |
| Deployment | Render         |
| Server     | Gunicorn       |

---

## 📂 Project Structure

```id="structure"
explain-ai-app/
│── templates/
│   └── explain.html
│── explain_app.py
│── requirements.txt
│── Procfile
│── README.md
│── .gitignore
```

---

## ⚙️ Run Locally

```bash id="clone"
git clone https://github.com/bhavyaah/explain-ai-app.git
cd explain-ai-app/explain-ai-app
```

```bash id="install"
pip install -r requirements.txt
```

Create `.env` file:

```env id="env"
API_KEY=your_api_key_here
```

Run:

```bash id="run"
python explain_app.py
```

Open:

```
http://127.0.0.1:5000
```

---

## ☁️ Deployment

Deployed on **Render** using:

* `gunicorn explain_app:app`
* Environment variables for API keys

---

## 🔐 Security

* API keys are stored in:

  * `.env` (local)
  * Render Environment Variables (production)

❌ Never commit secrets to GitHub

---

## ⚠️ Notes

* Free tier may sleep → first request takes ~30–50 sec
* API errors (401) = invalid/missing API key

---

## 🚧 Future Improvements

* 🎨 Better UI (Bootstrap / Tailwind)
* ⏳ Loading spinner
* 📜 Explanation history
* 📋 Copy/share button
* 🔑 User login system

---

## 👨‍💻 Author

**Bhavya**

---

## ⭐ Show some love

If you liked this project, drop a ⭐ on GitHub!
