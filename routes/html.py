from flask import Blueprint, render_template
from models import *
from db import db
html_bp = Blueprint("html", __name__)

@html_bp.route("/")
def home():
    return render_template("home.html")

@html_bp.route("/qa")
def q_and_a():
    return "q and a page"

@html_bp.route("/decks")
def decks():
    decks = db.session.execute(db.select(Deck)).scalars()
    return render_template("alldecks.html", data=decks)

@html_bp.route("/decks/<int:id>")
def deckcont(id):
    stmt = db.select(Cards).where(Cards.deck_id == id)
    exec = db.session.execute(stmt).scalars()
    return render_template("deck.html", data=exec)

@html_bp.route("/faq")
def faq():
    return render_template("faq.html")

@html_bp.route("/testcard")
def testcard():
    return render_template("testcard.html")

@html_bp.route("/Acards")
def allcards():
    cards = db.session.execute(db.select(Cards)).scalars()
    return render_template("allcards.html", data=cards)