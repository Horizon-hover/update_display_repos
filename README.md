# GitHub Repository Lister

A Python script that automatically generates a Markdown table of your GitHub repositories and updates your README.md file.

## 🚀 Features

- Fetches your public GitHub repositories via GitHub API
- Generates a clean Markdown table with repository details
- Automatically updates your README.md file
- Supports GitHub tokens for private repositories or higher rate limits

## ⚙️ Setup

1. **Install dependencies**:
   ```bash
   pip install requests
Configure the script:

Open github_repos_to_readme.py

Replace YOUR_GITHUB_USERNAME with your GitHub username

(Optional) Replace YOUR_GITHUB_TOKEN with a GitHub personal access token if you need to access private repos or avoid rate limits

Run the script:

python github_repos_to_readme.py
📊 Sample Output
The script will generate a Markdown table in your README.md that looks like:

## 📂 My GitHub Repositories

| Repository Name | Description | Link |
|---------------|-------------|------|
| **awesome-project** | My awesome project | [🔗 GitHub](https://github.com/user/awesome-project) |
| **cli-tool** | A useful CLI utility | [🔗 GitHub](https://github.com/user/cli-tool) |
🤖 Automation
For automatic updates, you can:

Add this script to a GitHub Action workflow

Set up a cron job to run it periodically

Run it manually whenever you want to update your README

📝 License
MIT License - Free for personal and commercial use