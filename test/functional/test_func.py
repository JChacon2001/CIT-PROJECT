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
    with test_client2.application.app_context():
        deck = Deck(name="Test Deck", description="Desc")
        db.session.add(deck)
        db.session.commit()
        deck_id = deck.id
        
        
    csv_data = "deck,question,answer\nDeck1,What is Flask?,A web framework\nDeck2,What is Python?,A programming language"
    
    data = {
        "deck": str(deck_id),
        "csv": (io.BytesIO(csv_data.encode("utf-8")), "test_import.csv")
    }

    response = test_client2.post(
        "/import", 
        data=data, 
        content_type="multipart/form-data"
    )

    assert response.status_code == 200
    expected_msg = f"Imported 2 cards into “{deck.name}”"
    assert expected_msg.encode() in response.data

    with test_client2.application.app_context():
        updated = db.session.execute(db.select(Deck).where(Deck.id == deck_id)).scalar()
        assert updated is not None
        assert len(updated.cards) == 2

       
        questions = {c.question for c in updated.cards}
        answers   = {c.answer   for c in updated.cards}

        assert "What is Flask?" in questions
        assert "A web framework" in answers
        assert "What is Python?" in questions
        assert "A programming language" in answers

def test_delete_decks(test_client2):
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
