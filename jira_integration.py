from jira import JIRA

# Jira configuration
JIRA_SERVER = 'https://your-jira-instance.com'
JIRA_USERNAME = 'your-username'
JIRA_PASSWORD = 'your-password'
JIRA_PROJECT = 'YOUR_PROJECT_KEY'

# Jira issue types
ISSUE_TYPES = {
    'Epic': 'Epic',
    'Story': 'Story',
    'Bug': 'Bug',
    'Task': 'Task'
}

# Jira custom field IDs
ROOT_CAUSE_FIELD_ID = 'customfield_123'
ENVIRONMENT_FIELD_ID = 'customfield_456'
LABELS_FIELD_ID = 'labels'

def create_subtasks(jira, parent_issue, component):
    # Create subtasks
    # ...

def create_jira_issue(selected_type, title, labels, root_cause, environment, flows):
    # Connect to Jira
    jira = JIRA(server=JIRA_SERVER, basic_auth=(JIRA_USERNAME, JIRA_PASSWORD))

    # Create main issue
    issue_type = ISSUE_TYPES[selected_type]
    issue = jira.create_issue(fields={
        'project': {'key': JIRA_PROJECT},
        'summary': title,
        'issuetype': {'name': issue_type},
        'labels': labels
    })

    # Set additional fields based on issue type
    if selected_type == 'Bug':
        issue.update(fields={ROOT_CAUSE_FIELD_ID: root_cause, ENVIRONMENT_FIELD_ID: environment})

    # Create subtasks
    subtasks = []
    subtasks.extend(create_subtasks(jira, issue, 'Epic'))
    subtasks.extend(create_subtasks(jira, issue, 'Story'))
    subtasks.extend(create_subtasks(jira, issue, 'Bug'))
    for flow in flows:
        subtasks.extend(create_subtasks(jira, issue, flow))

    print("Issue created successfully with key:", issue.key)
    print("Subtasks created successfully:")
    for subtask in subtasks:
        print(subtask.key, "-", subtask.fields.summary)
