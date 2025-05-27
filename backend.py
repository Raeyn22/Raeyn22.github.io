# backend/main.py
from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from supabase import create_client, Client
import os

app = FastAPI()

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Supabase setup
SUPABASE_URL = os.getenv("SUPABASE_URL", "https://your-project-ref.supabase.co")
SUPABASE_KEY = os.getenv("SUPABASE_KEY", "your-supabase-key")
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Models
class PriceAlertCreate(BaseModel):
    commodity: str
    target_price: float
    phone_number: str

class MarketPrice(BaseModel):
    commodity: str
    price: float
    market_location: str
    trend: str = "stable"

# Routes
@app.get("/")
def read_root():
    return {"message": "Supasoko API"}

@app.post("/price-alerts/")
def create_price_alert(alert: PriceAlertCreate, user_id: str = Depends(get_current_user)):
    # In a real app, you would:
    # 1. Save the alert to Supabase
    # 2. Set up a background task to monitor prices
    # 3. Send SMS when price is reached
    
    data, count = supabase.table("price_alerts").insert({
        "user_id": user_id,
        "commodity": alert.commodity,
        "target_price": alert.target_price,
        "phone_number": alert.phone_number
    }).execute()
    
    return {"message": f"Price alert set for {alert.commodity} at {alert.target_price}"}

@app.get("/market-prices/")
def get_market_prices(commodity: Optional[str] = None, location: Optional[str] = None):
    query = supabase.table("market_prices").select("*").order("reported_at", desc=True)
    
    if commodity:
        query = query.eq("commodity", commodity)
    if location:
        query = query.eq("market_location", location)
    
    data, count = query.execute()
    return data

# Helper functions
async def get_current_user(token: str = Depends(oauth2_scheme)):
    # In a real app, you would verify the JWT token
    try:
        # This is a simplified example
        user = supabase.auth.get_user(token)
        return user.id
    except Exception as e:
        raise HTTPException(status_code=401, detail="Invalid authentication")

# To run: uvicorn main:app --reload
