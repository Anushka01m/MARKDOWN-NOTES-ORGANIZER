import requests
import base64

def push_note_to_github(note):
    token = "your_github_token"
    repo = "your_username/your_repo"
    path = f"{note.vault}/{note.title.replace(' ', '_')}.md"
    content = base64.b64encode(note.content.encode()).decode()
    url = f"https://api.github.com/repos/{repo}/contents/{path}"
    headers = {"Authorization": f"token {token}"}
    data = {
        "message": f"Add note {note.title}",
        "content": content,
        "branch": "main"
    }
    requests.put(url, headers=headers, json=data)

