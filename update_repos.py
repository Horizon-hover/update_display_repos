import requests

# 🔹 Replace with your GitHub username & (optionally) token
USERNAME = "YOUR_GITHUB_USERNAME"
TOKEN = "YOUR_GITHUB_TOKEN"  # Optional, use for private repos or rate limits

# 🔹 GitHub API URL to fetch repositories
url = f"https://api.github.com/users/{USERNAME}/repos"
headers = {"Authorization": f"token {TOKEN}"} if TOKEN else {}

# 🔹 Fetch repositories
response = requests.get(url, headers=headers)

if response.status_code == 200:
    repos = response.json()

    # Generate Markdown Table
    md_table = "## 📂 My GitHub Repositories\n\n"
    md_table += "| Repository Name | Description | Link |\n"
    md_table += "|---------------|-------------|------|\n"

    for repo in repos:
        name = repo["name"]
        description = repo["description"] or "No description"
        link = repo["html_url"]
        md_table += f"| **{name}** | {description} | [🔗 GitHub]({link}) |\n"

    # Save to README.md
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(md_table)

    print("✅ Repository list updated in README.md")

else:
    print(f"❌ Failed to fetch repositories: {response.status_code}")
