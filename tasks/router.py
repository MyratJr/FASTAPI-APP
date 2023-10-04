from .tasks import send_email_report_dashboard
from random import randint

def get_dashboard_report(OTP:int=randint(1000,9999)):
    send_email_report_dashboard(OTP)
    return {
        "status": 200,
        "data": "Letter was sended",
        "details": None
    }
