import pytest
from models import Deck
from db import db

def test_main_page(test_client):
    response = test_client.get('/')
    assert response.status_code == 200
    assert b"Dashboard" in response.data


def test_faq_page(test_client):
    response = test_client.get('/faq')
    assert response.status_code == 200
    assert b"FAQs" in response.data

def test_unit_lib_page(test_client):
    response = test_client.get('/decks')
    assert response.status_code == 200
    assert b"Add Deck" in response.data

def test_allcards_page(test_client):
    response = test_client.get('/Acards')
    assert response.status_code == 200
    assert b"All" in response.data

def test_create_card_page(test_client):
    response = test_client.get('/card/new')
    assert response.status_code == 200
    assert b"Deck" in response.data 

def test_view_single_deck(test_client):
    response = test_client.get('card/edit/1')
    assert response.status_code == 200
    assert b"Question" in response.data 

def test_edit_card_page(test_client):
    response = test_client.get('card/edit/1')
    assert response.status_code == 200
    assert b"Question" in response.data 


def test_main_page_loads(test_client):
    response = test_client.get('/')
    assert response.status_code == 200


def test_create_new_deck_without_app(test_client):
    response = test_client.post(
        "/deck/new",
        data={
            "name": "Test Deck",
            "description": "A test deck description.",
            "category": "Science"  
        },
        follow_redirects=True
    )

    assert response.status_code == 200  

def test_create_deck_card(test_client):
    response = test_client.post(
        "/card/new",
        data={
            "deck": "Test Deck",
            "Question": "Say my name",
            "Answer": "I am Batman"  
        },
        follow_redirects=True
    )

    assert response.status_code == 200  


def test_create_new_deck(test_client2):
    response = test_client2.post(
        "/deck/new",
        data={
            "name": "Test Deck",
            "description": "A test deck description.",
            "category": "Science"  
        },
        follow_redirects=True
    )

    assert response.status_code == 200  

    with test_client2.application.app_context():
        from models import Deck, Category

        deck = Deck.query.filter_by(name="Test Deck").first()
        assert deck is not None
        assert deck.description == "A test deck description."
        assert deck.category is not None
        assert deck.category.name == "Science"
