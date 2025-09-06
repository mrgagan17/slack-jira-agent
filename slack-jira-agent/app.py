from slack_handler import get_slack_messages
from ai_agent import process_message
from jira_handler import create_jira_ticket, mark_task_done

def main():
    print("🤖 Custom GPT Agent Started...\n")

    messages = get_slack_messages()

    for msg in messages:
        print(f"📩 New Slack Message: {msg}")
        task = process_message(msg)

        if task:
            issue_key = create_jira_ticket(task)

            # Automatically mark done if message contains keyword "done"
            if "done" in msg.lower():
                mark_task_done(issue_key)

if __name__ == "__main__":
    main()
