from .tasks import send_email_report_dashboard

def get_dashboard_report(username:str,email:str,OTP:int):
    send_email_report_dashboard(username,email,OTP)
    return {
        "status": 200,
        "data": "Letter was sended",
        "details": None
    }
