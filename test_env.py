from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=os.path.join(os.getcwd(), ".env"))

print("DATABASE_URL =", os.getenv("DATABASE_URL"))
