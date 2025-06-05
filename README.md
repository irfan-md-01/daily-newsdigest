# 📰 Daily-NewsDigest – Automated Python Newspaper Distribution system
#### Video Demo:  https://youtu.be/gsgqBy9fEwo
#### Description:
I developed an automated newspaper generation system in Python that fetches real-time news articles using a public API, formats them into a well-structured PDF using ReportLab, and delivers the final document via email to a list of subscribers. The entire process is fully automated using GitHub Actions, enabling daily delivery without any manual intervention. Subscriber emails are managed through a Google Form connected to a Google Sheet, which the script accesses securely via the Google Sheets API. Credentials and API keys are safely handled using GitHub Secrets. 

![Python](https://img.shields.io/badge/Built%20With-Python-blue)
![Status](https://img.shields.io/badge/Automation-GitHub%20Actions-success)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

## 📌 Features

- 📰 Fetches live news articles from an API (e.g., NewsAPI)
- 📝 Converts articles into a clean, formatted PDF
- ✉️ Emails the PDF to all subscribers
- 📅 Scheduled daily via **GitHub Actions** (no hosting needed)
- 🧾 Subscribers managed via **Google Forms + Google Sheets**
- 🔒 API key, credentials, and recipient list securely managed with GitHub Secrets

---

## 🧠 Tech Stack

- Python (requests, gspread, reportlab)
- Google Sheets API
- Gmail SMTP
- GitHub Actions (for automation)
- Google Forms (for subscriptions)

---

## 📂 Project Structure

```bash
.
├── make_newspaper.py         # Main script
├── subscriber_fetcher.py     # Fetch emails from Google Sheets
├── requirements.txt
├── credentials.json          # Created from GitHub Secret at runtime
├── .github/
│   └── workflows/
│       └── daily_news.yml    # GitHub Actions workflow
.
