import smtplib
from email.message import EmailMessage
from celery import Celery
from config import SMTP_USER, SMTP_PASSWORD


SMTP_HOST="smtp.gmail.com"
SMTP_PORT=465

celery=Celery('tasks',broker='redis://localhost:6379')

def get_email_template_dashboard(username,email1,OTP):
    email=EmailMessage()
    email['Subject']='Account verification code'
    email['From']=SMTP_USER
    email['To']=email1
    email.set_content(
        '<div>'
        f'<h1>Hello {username}, this is your verification code. Go to the program and verify your account: <h2 style="font-size:50px">{OTP}</h2></h1>'
        '</div>',
        subtype='html'
    )
    return email

@celery.task
def send_email_report_dashboard(username,email,OTP):
    email=get_email_template_dashboard(username,email,OTP)
    with smtplib.SMTP_SSL(SMTP_HOST,SMTP_PORT) as server:
        server.login(SMTP_USER, SMTP_PASSWORD)
        server.send_message(email)