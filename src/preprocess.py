import re
from bs4 import BeautifulSoup
try:
    nltk.data.find("corpora/stopwords")
 Lark except LookupError:
    nltk.download("stopwords")
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

stp = stopwords.words("english")


def clean_text(text):
    text = text.lower()

    soup = BeautifulSoup(text, "html.parser")
    text = soup.get_text(separator=" ")

    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)

    lem = WordNetLemmatizer()
    text = " ".join([lem.lemmatize(w) for w in text.split()])

    text = " ".join([w for w in text.split() if w not in stp])

    return text
