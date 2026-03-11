import requests

BOT_TOKEN = "8763118689:AAHxZshgFCTiK8Z4YgGhD5ls-qMkg2s_ric"
CHAT_ID = "1926772196"

def send_notification(message):

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    data = {
        "chat_id": CHAT_ID,
        "text": message
    }

    response = requests.post(url, data =data)
    print("Notification sent:", response.status_code)

