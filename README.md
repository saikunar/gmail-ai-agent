# Gmail AI Agent

This project is a simple AI automation system that connects to Gmail, checks incoming emails, detects spam messages, and sends notifications to Telegram for important emails.

The goal of this project is to automate email monitoring and reduce the time spent checking emails manually.

---

## What This Project Does

• Connects to Gmail using Gmail API  
• Reads new emails from the inbox  
• Detects spam emails using a simple detection logic  
• Moves spam emails to the spam folder automatically  
• Sends notifications to Telegram when a new important email arrives  
• Generates a short summary of the email subject  

---

## How the System Works

1. The program connects to Gmail using the Gmail API.  
2. It checks the inbox every 2 minutes.  
3. Each email is analyzed by the spam detection module.  
4. If the email is spam, it is moved to the spam folder.  
5. If the email is not spam, the system summarizes it and sends a notification to Telegram.  

This allows the user to monitor important emails directly from their phone.

---

## Technologies Used

Python  
Gmail API  
Telegram Bot API  
Requests Library  

---

## Project Files

```
gmail-ai-agent/
│
├── main.py                # Main program that runs the AI agent
├── gmail_reader.py        # Connects to Gmail and reads emails
├── ml_spam_detector.py    # Detects spam emails
├── email_summarizer.py    # Creates a short summary of the email
├── notifier.py            # Sends Telegram notifications
├── requirements.py        # Required Python libraries
└── README.md
```

---

## How to Run the Project

1. Clone the repository

```
git clone https://github.com/yourusername/gmail-ai-agent.git
```

2. Install required libraries

```
pip install -r requirements.txt
```

3. Add Gmail API credentials

Place the `credentials.json` file in the project folder.

4. Run the program

```
python main.py
```

The system will start checking emails automatically.

---

## Future Improvements

Some features that can be added in the future:

• AI-based email summarization using large language models  
• Automatic email reply generation  
• Priority email detection (important emails)  
• Deploying the system on cloud for 24/7 monitoring  

---

## Author

V.M. Sai Kumar  
AI / Machine Learning Engineer
