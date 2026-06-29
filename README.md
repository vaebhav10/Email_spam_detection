
# Email Spam Detection

### Overview 
This project pipeline uses classical ML to detect/classify an email Ham/Spam.

It works on the *tfidf principle* i.e: tracking the kind of words that appears in spam/ham message.

## How to run/Installation:
clone the repo:
```bash
git clone https://github.com/vaebhav10/Email_spam_detection.git
cd Email_spam_detection
```
### Create a venv and install dependencies(for linux/macOS) :

Use python3.10 version for smooth workflow
```bash
python3.10 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
Execute the `main.py` to get the classification/prediction on a custom email as ham/spam locally.

**Limitations:**  
Since this project uses tfidf vectorization it does not understand the semantic meaning of texts in the Email and classifies them only based on the count of certain words that appear in the Email/text.

## Deployement:
A streamlit dashboard is provided for the interactive prediction of an Email.
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://vaebhav10-email-spam-detection-app-oqnbt1.streamlit.app/)
