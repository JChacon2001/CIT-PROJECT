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


# def test_deck_creation(test_client):
#     resp = test_client.post(
#         "/deck/new",
#         data={
#             "name": "test deck",
#             "description": "Testing",
#             "category": "Cats"
#         },
#         follow_redirects=True
#     )
#     assert resp.status_code == 200

    

#     with test_client.application.app_context():
#         deckstest = db.session.query(Deck).filter_by(name="test deck").all()
#         # assert len(deckstest) == 1
#         # print(deckstest)
#         assert deckstest[1].description == "Testing"
