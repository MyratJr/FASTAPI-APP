from dotenv import load_dotenv
import os

load_dotenv()

ACCESS_TOKEN_EXPIRE_MINUTES=int(os.environ.get("ACCESS_TOKEN_EXPIRE_MINUTES"))
ALGORITHM=os.environ.get("ALGORITHM")
JWT_SECRET_KEY = os.environ['JWT_SECRET_KEY']