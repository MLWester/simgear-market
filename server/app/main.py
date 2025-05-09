from fastapi import FastAPI
from sqlalchemy import create_engine
from app import config

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "SimGear Market API is running"}

@app.on_event("startup")
def test_db_connection():
    if not config.DATABASE_URL:
        print("❌ DATABASE_URL is not set in .env")
        return

    try:
        engine = create_engine(config.DATABASE_URL)
        with engine.connect() as conn:
            print("✅ Connected to the PostgreSQL database")
    except Exception as e:
        print("❌ Failed to connect to the database:", e)

if not config.JWT_SECRET:
    print("⚠️ JWT_SECRET not set.")
if not config.STRIPE_KEY:
    print("⚠️ STRIPE_KEY not set.")

# ✅ Add this route to test proxy from frontend
@app.get("/api/test")
def test_proxy():
    return {"message": "Proxy is working!"}
