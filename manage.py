from app import app
from db import db
import csv
from sqlalchemy import select, func
from models import Cards, Deck

file = "flashcard.csv"

def load_csv(filename):
    with open(filename, 'r', encoding='utf-8') as csvfile:
        csvreader = csv.DictReader(csvfile)
       
        for row in csvreader:
            deck_name = row["deck"]
           
            deck_obj = db.session.execute(select(Deck).where(Deck.name == deck_name)).scalar()
           
            if not deck_obj:
                deck_obj = Deck(name=deck_name, description="Default description")
                db.session.add(deck_obj)
           
            cards = Cards(deck=deck_obj, question=row["question"], answer=row["answer"])
           
            db.session.add(cards)
       
        db.session.commit()

def drop_tables():
    db.drop_all()
    db.session.commit()

def create_tables():
    db.create_all()

if __name__ == "__main__":
    with app.app_context():
        drop_tables()
        create_tables()
        load_csv(file)