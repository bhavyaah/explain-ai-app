from flask import Flask, render_template, request
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Load data
df = pd.read_csv("spam.csv", sep="\t", names=["label", "message"])
df['label'] = df['label'].map({'ham': 0, 'spam': 1})

# Train model
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df['message'])

model = MultinomialNB()
model.fit(X, df['label'])

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    msg = request.form['message']
    vec = vectorizer.transform([msg])
    result = model.predict(vec)[0]
    return render_template('index.html', prediction="Spam" if result else "Not Spam")

if __name__ == "__main__":
    app.run(debug=True)