import pytest
from models import Deck, Category, Cards
from db import db

def test_db_schema(test_client2):
    with test_client2.application.app_context():

        category = Category(name="Original Category")
        db.session.add(category)
        db.session.commit()


        deck = Deck(name="Original Deck", description="Original Description", category_id=category.id)
        db.session.add(deck)
        db.session.commit()


        card = Cards(question="Original Question", answer="Original Answer", deck_id=deck.id)
        db.session.add(card)
        db.session.commit()


        fetched_category = db.session.get(Category, category.id)
        fetched_deck = db.session.get(Deck, deck.id)
        fetched_card = db.session.get(Cards, card.id)

        assert fetched_category.name == "Original Category"
        assert fetched_deck.name == "Original Deck"
        assert fetched_card.question == "Original Question"

        fetched_category.name = "Updated Category"
        fetched_deck.name = "Updated Deck"
        fetched_deck.description = "Updated Description"
        fetched_card.question = "Updated Question"
        fetched_card.answer = "Updated Answer"
        db.session.commit()

        updated_category = db.session.get(Category, category.id)
        updated_deck = db.session.get(Deck, deck.id)
        updated_card = db.session.get(Cards, card.id)

        assert updated_category.name == "Updated Category"
        assert updated_deck.name == "Updated Deck"
        assert updated_deck.description == "Updated Description"
        assert updated_card.question == "Updated Question"
        assert updated_card.answer == "Updated Answer"
