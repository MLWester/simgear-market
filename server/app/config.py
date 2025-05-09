import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("postgresql://postgres:Mlw412214@localhost:5432/simgear_market")
JWT_SECRET = os.getenv("JWT_SECRET")
STRIPE_KEY = os.getenv("STRIPE_KEY")
