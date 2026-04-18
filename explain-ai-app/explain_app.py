from flask import Flask, render_template, request
import requests
import os
from dotenv import load_dotenv

load_dotenv()   # 1. load env FIRST

app = Flask(__name__)

API_KEY = os.getenv("API_KEY")   # 2. get key

if not API_KEY:                  # 3. THEN check
    raise ValueError("API key not found")
@app.route('/')
def home():
    return render_template('explain.html')
@app.route('/explain', methods=['POST'])
def explain():
    topic = request.form.get('topic')
    level = request.form.get('level')
    if not topic or not level:
        return render_template('explain.html', result="Please enter both topic and level.")
    prompt = f"Explain {topic} in {level} level in simple terms with examples."
    try:
        response = requests.post(
    "https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost:5000",
        "X-Title": "Explain AI App"
    },
    json={
        "model": "openai/gpt-3.5-turbo",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }
)
        data = response.json()
        print("API RESPONSE:", data)  # debug
        if 'choices' in data:
            result = data['choices'][0]['message']['content']
        else:
            result = f"API Error: {data}"
    except Exception as e:
        result = f"Error: {str(e)}"
    return render_template('explain.html', result=result)
if __name__ == '__main__':
    app.run(debug=True)
