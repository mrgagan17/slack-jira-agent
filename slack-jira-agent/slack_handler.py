from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from config import SLACK_TOKEN, SLACK_CHANNEL_ID

client = WebClient(token=SLACK_TOKEN)

def get_slack_messages():
    """Fetch latest messages from Slack channel"""
    try:
        response = client.conversations_history(channel=SLACK_CHANNEL_ID, limit=5)
        messages = [msg["text"] for msg in response["messages"]]
        return messages
    except SlackApiError as e:
        print(f"❌ Error fetching Slack messages: {e.response['error']}")
        return []
