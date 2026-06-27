from pathlib import Path
import joblib
from src.preprocess import clean_text

path = Path(__file__).resolve().parent.parent
model = joblib.load(path / "models/svm_model.pkl")
tfidf = joblib.load(path / "models/tfidf.pkl")


def predict(text):

    text = clean_text(text)
    text = tfidf.transform([text])

    pred = model.predict(text)[0]
    return "Spam" if pred else "Ham/Not Spam"
