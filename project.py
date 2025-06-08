from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus.flowables import HRFlowable
from datetime import datetime, date
import requests
import json
from io import BytesIO
from time import sleep
from argparse import ArgumentParser
from email.message import EmailMessage
import os
import smtplib
from validator_collection import validators
import sys
from load_subscribers import get_subscriber
import traceback
from dotenv import load_dotenv

class PyNewsPdf:

    def __init__(self):
        self.doc = SimpleDocTemplate(f"NewsPaper_{date.today()}.pdf", pagesize=A4)
        self.styles = getSampleStyleSheet()
        self.elements = []

        self.title_style = ParagraphStyle(
            name="TitleStyle", fontSize=22, alignment=TA_CENTER, spaceAfter=15)
        self.date_style = ParagraphStyle(
            name="DateStyle", fontSize=12, alignment=TA_CENTER, spaceAfter=20)
        self.article_title_style = ParagraphStyle(
            name="ArticleTitle", parent=self.styles["Heading3"], spaceAfter=5)
        self.body_style = self.styles["BodyText"]
        self.link_style = ParagraphStyle(
            name="Link", parent=self.styles["Normal"], textColor=colors.blue, fontSize=10)

        self.elements.append(Paragraph("News Paper Digest", self.title_style))
        self.elements.append(
            Paragraph(f"Date: {datetime.now().strftime('%B %d, %Y')}", self.date_style))

    def add_news(self, articles: dict, category: str):
        self.elements.append(Paragraph(category.title(), self.article_title_style))
        self.elements.append(HRFlowable(
            width="100%", thickness=0.7, color=colors.grey))
        self.elements.append(Spacer(1, 6))

        for article in articles:

            self.elements.append(
                Paragraph(article["title"], self.article_title_style))
            desc = Paragraph(article["description"], self.body_style)

            img = None
            if article.get("image"):
                try:
                    response = requests.get(article["image"])
                    if response.status_code == 200:
                        img_data = BytesIO(response.content)
                        img = Image(img_data, width=150, height=100)
                        time.sleep(1)
                except:
                    pass

            if img:
                table_data = [[desc, img]]
                col_widths = [370, 150]
            else:
                table_data = [[desc]]
                col_widths = [520]

            table = Table(table_data, colWidths=col_widths)
            table.setStyle(TableStyle([
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
            ]))
            self.elements.append(table)
            self.elements.append(Spacer(1, 6))

            self.elements.append(
                Paragraph(article["content"], self.body_style))
            self.elements.append(Spacer(1, 6))
            link = f'<link href="{article["url"]}">Read More</link>'
            self.elements.append(Paragraph(link, self.link_style))
            self.elements.append(Spacer(1, 20))

    def save(self):
        self.doc.build(self.elements)
        self.elements = []


class PyNewsRead:

    def __init__(self):
        self.apikey = os.getenv("API_KEY")
        self.pdfwrite = PyNewsPdf()

    def get_headlines(self):
        categories = ["technology", "nation", "business", "world",
                      "entertainment", "sports", "science", "health", "general"]

        for category in categories:
            response = requests.get(
                f"https://gnews.io/api/v4/top-headlines?category={category}&lang=en&max=7&apikey={self.apikey}")
            news = json.loads(response.text)

            self.pdfwrite.add_news(news["articles"], category)
            if category=="business":
                break
            sleep(2)

        self.pdfwrite.save()

    def share_email(self, email: tuple):
        my_mail = os.getenv("MY_MAIL")
        my_pass = os.getenv("EMAIL_PASSWORD")

        try :
                msg = EmailMessage()
                msg['From'] = my_mail
                msg['To'] = email
                msg['Subject'] = f"Your Weekly Newspaper – {datetime.now().strftime('%B %d, %Y')}"
                body = f"""Dear Reader,\n
Please find attached your copy of the newspaper for {datetime.now().strftime('%B %d, %Y')}.\n
We hope you enjoy reading it. If you have any feedback or suggestions, feel free to reach out to us.\n
Best regards,\n
Newspaper Team
"""
                msg.set_content(body)
                pdf_file = f"NewsPaper_{date.today()}.pdf"
            
                with open(pdf_file, 'rb') as f:
                    file_data = f.read()
                    msg.add_attachment(file_data, maintype='application', subtype='pdf', filename=pdf_file)

                with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                    smtp.login(my_mail, my_pass)
                    smtp.send_message(msg)
                    print("Email sent successfully!")
    
        except:
            traceback.print_exc()
            sys.exit("error occured in email function")

def main():
    p = PyNewsRead()
    p.get_headlines()
    
    # emails = get_subscriber()
    emails = os.getenv("RECIPIENTS")
    p.share_email(emails)


if __name__ == "__main__":
    try :
        load_dotenv()
        main()
    except:
        traceback.print_exc()
        sys.exit()
