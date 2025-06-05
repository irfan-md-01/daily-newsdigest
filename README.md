# 📰 Daily-NewsDigest – Automated Python Newspaper Distribution system
#### Video Demo:  https://youtu.be/gsgqBy9fEwo
#### Description:
Generate a personalized daily newspaper in PDF format, fetch the latest headlines using APIs, and email it to your subscribers — all fully automated using GitHub Actions and Google Sheets.

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
