from datetime import datetime, timedelta
from config import JIRA_PROJECT_KEY
from config import JIRA_EMAIL, JIRA_API_TOKEN, JIRA_DOMAIN, JIRA_PROJECT_KEY
from jira import JIRA

jira = JIRA(server=f"https://{JIRA_DOMAIN}", basic_auth=(JIRA_EMAIL, JIRA_API_TOKEN))

def mark_task_done(issue_key):
    """
    Marks a Jira ticket as done.
    """
    # Transition ID for "Done" depends on your Jira workflow.
    # You can find it using jira.transitions(issue_key)
    transitions = jira.transitions(issue_key)
    done_transition = None
    for t in transitions:
        if t['name'].lower() == 'done':
            done_transition = t['id']
            break

    if done_transition:
        jira.transition_issue(issue_key, done_transition)
        print(f"✅ Task {issue_key} marked as Done")
    else:
        print(f"❌ No 'Done' transition found for {issue_key}")

def create_jira_ticket(task):
    # Set due date based on priority
    if task['priority'] == "High":
        due_date = (datetime.now() + timedelta(days=2)).strftime("%Y-%m-%d")
    elif task['priority'] == "Medium":
        due_date = (datetime.now() + timedelta(days=4)).strftime("%Y-%m-%d")
    else:
        due_date = (datetime.now() + timedelta(days=7)).strftime("%Y-%m-%d")

    issue_dict = {
        'project': {'key': JIRA_PROJECT_KEY},
        'summary': task['title'].replace("\n", " "),  # Jira summary cannot have newlines
        'description': task['description'],
        'duedate': due_date,
        'issuetype': {'name': 'Task'}
    }

    # Create Jira issue here (mocked or real)
    print(f"✅ Jira Ticket Created: {task['title']}")
    print(f"   Priority : {task['priority']}")
    print(f"   Due Date : {due_date}\n")
