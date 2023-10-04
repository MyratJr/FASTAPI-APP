from fastapi import HTTPException

def exchand(status_c, detail_c):
    raise HTTPException(status_c ,detail_c)