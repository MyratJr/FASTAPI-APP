import smtplib
from email.message import EmailMessage
from celery import Celery
from config import SMTP_USER, SMTP_PASSWORD, SMTP_USER_TO

SMTP_HOST="smtp.gmail.com"
SMTP_PORT=465

celery=Celery('tasks',broker='redis://localhost:6379')

def get_email_template_dashboard(OTP:int):
    email=EmailMessage()
    email['Subject']='Report from BEST TRADING Platform'
    email['From']=SMTP_USER
    email['To']=SMTP_USER_TO
    email.set_content(
        '<div>'
        f'<h1>Hello, this is your verification code: <h2 style="font-size:50px">{OTP}</h2></h1>'
        '</div>',
        subtype='html'
    )
    return email

@celery.task
def send_email_report_dashboard(OTP:int):
    email=get_email_template_dashboard(OTP)
    with smtplib.SMTP_SSL(SMTP_HOST,SMTP_PORT) as server:
        server.login(SMTP_USER, SMTP_PASSWORD)
        server.send_message(email)