from fastapi import FastAPI
from dotenv import load_dotenv
import os
from sqlalchemy import create_engine

# Load environment variables from .env file
load_dotenv()

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "SimGear Market API is running"}

# Test DB connection on startup
@app.on_event("startup")
def test_db_connection():
    db_url = os.getenv("DATABASE_URL")
    if not db_url:
        print("❌ DATABASE_URL is not set in .env")
        return

    try:
        engine = create_engine(db_url)
        with engine.connect() as conn:
            print("✅ Connected to the PostgreSQL database")
    except Exception as e:
        print("❌ Failed to connect to the database:", e)
