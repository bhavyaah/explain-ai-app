import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# Load dataset
df = pd.read_csv("spam.csv", sep="\t", names=["label", "message"])

# Convert labels
df['label'] = df['label'].map({'ham': 0, 'spam': 1})

# Split data
X_train, X_test, y_train, y_test = train_test_split(df['message'], df['label'], test_size=0.2)

# Feature extraction
vectorizer = CountVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Train model
model = MultinomialNB()
model.fit(X_train_vec, y_train)

# Predictions
y_pred = model.predict(X_test_vec)

print("Accuracy:", accuracy_score(y_test, y_pred))

# Test your own message
while True:
    user_input = input("Enter message: ")
    vec = vectorizer.transform([user_input])
    print("Spam" if model.predict(vec)[0] else "Not Spam")