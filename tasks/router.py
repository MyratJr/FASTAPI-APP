from fastapi import APIRouter, Depends
from .tasks import send_email_report_dashboard
from .utils import get_current_user

router = APIRouter(prefix="/report")

@router.get("/dashboard")
async def get_dashboard_report(user=Depends(get_current_user)):
    send_email_report_dashboard.delay(user["User"])
    return {
        "status": 200,
        "data": "Letter was sended",
        "details": None
    }
