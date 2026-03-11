from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Training data
emails = [
    "Win lottery now",
    "Free money offer",
    "Urgent prize claim",
    "Meeting tomorrow",
    "Project discussion",
    "Lunch plans today"
]

labels = [
    "SPAM",
    "SPAM",
    "SPAM",
    "NOT SPAM",
    "NOT SPAM",
    "NOT SPAM"
]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(emails)

model = MultinomialNB()
model.fit(X, labels)


def detect_spam_ml(email_text):

    X_test = vectorizer.transform([email_text])

    prediction = model.predict(X_test)

    return prediction[0]