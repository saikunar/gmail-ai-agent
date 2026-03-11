from gmail_reader import read_emails, move_to_spam
from ml_spam_detector import detect_spam_ml
from notifier import send_notification
from email_summarizer import summarize_email
import time


def run_ai_agent():

    print("Gmail AI Agent Started...")

    while True:

        print("\nChecking for new emails...")

        emails = read_emails()

        for email in emails:

            subject = email["subject"]
            message_id = email["id"]

            print("\nEmail:", subject)

            result = detect_spam_ml(subject)

            print("AI Decision:", result)

            # SPAM handling
            if result == "SPAM":
                move_to_spam(message_id)

            # IMPORTANT EMAIL
            else:
                summary = summarize_email(subject)

        send_notification(
    f"📧 New Important Email\n\nSubject: {subject}\n\nAI Summary:\n{summary}"
)
        print("\nWaiting 2 minutes before next check...")

        time.sleep(120)


if __name__ == "__main__":
    run_ai_agent()