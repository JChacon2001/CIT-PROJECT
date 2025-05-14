import pytest
from models import Deck
from db import db
from models import Deck, Category, Cards
import io
import csv

def test_error_page(test_client2):
    resp = test_client2.get("/randompg", follow_redirects = False)
    assert resp.status_code == 404

def test_create_full_stack(test_client2):
    with test_client2.application.app_context():
        cat = Category(name="Science")
        db.session.add(cat)
        db.session.commit()

        deck = Deck(name="Physics", description="Basics", category_id=cat.id)
        db.session.add(deck)
        db.session.commit()

        card = Cards(question="What is gravity?", answer="A force", deck_id=deck.id)
        db.session.add(card)
        db.session.commit()

        assert card.deck.name == "Physics"
        assert card.deck.category.name == "Science"


def test_import_csv(test_client2):
    csv_data = "deck,question,answer\nDeck1,What is Flask?,A web framework\nDeck2,What is Python?,A programming language"
    
    data = {
        "csv": (io.BytesIO(csv_data.encode("utf-8")), "test_import.csv")
    }

    response = test_client2.post(
        "/import", 
        data=data, 
        content_type="multipart/form-data"
    )

    assert response.status_code == 200
    assert b"Upload successful" in response.data

    with test_client2.application.app_context():
        deck1 = db.session.execute(db.select(Deck).where(Deck.name == "Deck1")).scalar()
        deck2 = db.session.execute(db.select(Deck).where(Deck.name == "Deck2")).scalar()

        assert deck1 is not None
        assert deck2 is not None
        assert len(deck1.cards) == 1  
        assert len(deck2.cards) == 1

def test_detete_decks(test_client2):
    csv_data = "deck,question,answer\nDeck1,What is Flask?,A web framework\nDeck2,What is Python?,A programming language"
    
    data = {
        "csv": (io.BytesIO(csv_data.encode("utf-8")), "test_import.csv")
    }

    response = test_client2.post(
        "/import", 
        data=data, 
        content_type="multipart/form-data"
    )
    response = test_client2.get("http://127.0.0.1:5000/deck/delete/2")
    assert response.status_code == 302
