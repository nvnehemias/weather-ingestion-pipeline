from dotenv import load_dotenv
import os 

# Load variables from the .env file 
load_dotenv()

DB_USER = os.getenv("DB_USER","postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD","")
DB_HOST = os.getenv("DB_HOST","localhost")


raw_port = os.getenv("DB_PORT")
DB_PORT = raw_port if raw_port and raw_port.strip() != "" else "5432"

DB_NAME = os.getenv("DB_NAME","postgres")
