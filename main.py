from fastapi import FastAPI, Form
from fastapi.responses import Response
from fastapi.middleware.cors import CORSMiddleware
from conversation import process_message
from db import SessionLocal, Base, engine
from models import Review
from sqlalchemy import inspect

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# this creates tables reviews if it does not exists in the db
inspector = inspect(engine)
if not inspector.has_table("reviews"):
    Base.metadata.create_all(bind=engine)
    print("Table created")
else:
    print("table existed")

@app.post("/whatsapp/webhook")
def whatsapp_webhook(From: str = Form(...), Body: str = Form(...)):
    reply = process_message(From, Body)
    return Response(
        content=f"<Response><Message>{reply}</Message></Response>",
        media_type="application/xml"
    )

@app.get("/api/reviews")
def get_reviews():
    db = SessionLocal()
    reviews = db.query(Review).all()
    db.close()
    return reviews

@app.get("/")
def root():
    return {"message": "FastAPI WhatsApp Review Collector is running!"}
