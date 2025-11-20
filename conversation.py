from db import SessionLocal
from models import Review
from datetime import datetime


user_states = {}

def process_message(from_number, message):
    """
    handles the conversation very basic flow right now
    """
    db = SessionLocal()
    contact = from_number.strip()
    text = message.strip()

   
    state = user_states.get(contact, {"step": 0})

    
    if state["step"] == 0:
        user_states[contact] = {"step": 1}
        return "Hello! Which product would you like to review?"

    
    elif state["step"] == 1:
        state["product"] = text
        state["step"] = 2
        user_states[contact] = state
        return "Got it. What is your name?"

    
    elif state["step"] == 2:
        state["user"] = text
        state["step"] = 3
        user_states[contact] = state
        return f"Thank you, {state['user']}. Please type your review for {state['product']}."
    


    
    elif state["step"] == 3:
        #didnt wanted to share my number so hardcoded it for the whatsapp:12235435 number format
        masked_number=from_number.split(":")
        masked_number=masked_number[1]
        masked_number=masked_number[0:3]+"****"+masked_number[-2:]
        review = Review(
            contact_number=masked_number,
            user_name=state["user"],
            product_name=state["product"],
            product_review=text,
            created_at=datetime.utcnow(),
        )

        db.add(review)
        db.commit()
        db.close()

        reply = (
            f"Thanks {state['user']}. Your review for {state['product']} has been recorded."
        )

        user_states.pop(contact, None)
        return reply

    #resrt condition
    else:
        user_states.pop(contact, None)
        return "Let's start again. Which product would you like to review?"
