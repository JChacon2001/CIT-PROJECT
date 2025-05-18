from app import app
from db import db
import csv
from sqlalchemy import select, func
from models import Cards, Deck, Category

file = "flashcard.csv"

def load_csv(filename):
    with open(filename, 'r', encoding='utf-8') as csvfile:
        csvreader = csv.DictReader(csvfile)
       
        for row in csvreader:
            
            course_name = row["category"]
            course_obj = db.session.execute(select(Category).where(Category.name == course_name)).scalar()
            if not course_obj:
                course_obj = Category(name=course_name)
                db.session.add(course_obj)
            
            deck_name = row["deck"]

            deck_obj = db.session.execute(select(Deck).where(Deck.name == deck_name).where(Deck.category_id == course_obj.id)).scalar()
            
            if not deck_obj:
                deck_obj = Deck(name=deck_name, description="Default description", category=course_obj)
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