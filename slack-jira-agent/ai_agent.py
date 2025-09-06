def process_message(message):
    """
    Simple AI agent for demo.
    Adds priority based on keywords.
    """
    message_clean = message.replace("\n", " ").strip()
    if "fix" in message.lower() or "bug" in message.lower():
        priority = "High"
    elif "feature" in message.lower():
        priority = "Medium"
    else:
        priority = "Low"

    task = {
        "title": f"Task: {message_clean[:50]}...",  # safe title
        "description": message_clean,
        "priority": priority
    }
    return task
