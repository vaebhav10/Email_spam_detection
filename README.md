
# Email Spam Detection

### Overview 
This project pipeline uses classical ML to detect/classify an email Ham/Spam.

This project uses a deep learning pipeline to classify emails/messages as Spam or Ham.

The current model is based on an LSTM (Long Short-Term Memory) architecture, which processes tokenized text sequences and learns contextual patterns in message content.
A TextVectorization layer is used to convert raw text into padded integer sequences before inference.
  
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

## Deployement:
A streamlit dashboard is provided for the interactive prediction of an Email.
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)]([https://vaebhav10-email-spam-detection-app-oqnbt1.streamlit.app/](https://vaebhav10-email-spam-detection-app-0fulni.streamlit.app/))
