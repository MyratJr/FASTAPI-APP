from fastapi import Depends,HTTPException
from jwt_.bearer import is_logged_in

def get_current_user(is_logged:bool=Depends(is_logged_in)):
    if is_logged is False:
        raise HTTPException(status_code=401,detail="Any user have not logged in.")
    return {'User':is_logged}