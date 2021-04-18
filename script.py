import schedule
import time
from decouple import config
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

TOKEN = config('TOKEN_KEY')
channel = '#일반'
message = '한 주도 수고했어요 :relaxed:'

client = WebClient(token=TOKEN)


def slacker():
    try:
        response = client.chat_postMessage(channel=channel, text=message)
        print(response)
        assert response['message']['text'] == message
    except SlackApiError as error:
        assert error.response['ok'] is False
        assert error.response['error']
        print(f"yourethebest-bot got error: {error.response['error']}")

schedule.every().sunday.at('15:00').do(slacker)

while True:
    schedule.run_pending()
    time.sleep(1)
