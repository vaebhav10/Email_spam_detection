import re
from bs4 import BeautifulSoup
import nltk
try:
    nltk.data.find("corpora/stopwords")
except LookupError:
    nltk.download("stopwords")

try:
    nltk.data.find("corpora/wordnet")
except LookupError:
    nltk.download("wordnet")
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

stp = stopwords.words("english")
lem = WordNetLemmatizer()

def cleanup(text):
    text = text.lower()

    soup = BeautifulSoup(text, 'html.parser')
    text = soup.get_text(separator = ' ')

    text = re.sub(r'[^a-zA-Z0-9\s]',' ', text)

    text = ' '.join([lem.lemmatize (w) for w in text.split()])
    
    text = ' '.join([w for w  in text.split() if w not in stp])
    
    return text 
