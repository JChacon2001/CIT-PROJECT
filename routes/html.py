from flask import Blueprint, render_template, redirect, url_for
from models import *
from forms import DeckForm, CardForm, EditCardForm
from db import db
html_bp = Blueprint("html", __name__)

@html_bp.route("/")
def home():
    top4 = db.session.execute(db.select(Deck).limit(4)).scalars()
    decks = db.session.execute(db.select(Deck)).scalars()
    return render_template("home.html", top4=top4, Deck=decks)

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

@html_bp.route("/deck/new", methods=['GET', 'POST'])
def deck_form(id=None):
    form = DeckForm()
    
    if form.validate_on_submit():
        new_deck = Deck(name=form.name.data, description=form.description.data)
        db.session.add(new_deck)
        db.session.commit()
    
        return redirect(url_for("html.decks"))

    return render_template("create_deck.html", form=form)

@html_bp.route('/card/new', methods=['GET', 'POST'])
def create_card():
    form = CardForm()
    stmt = db.select(Deck).order_by(Deck.name)
    decks = db.session.execute(stmt).scalars()
    form.deck.choices = []
    for deck in decks:
        form.deck.choices.append((deck.id, deck.name))

    if form.validate_on_submit():
        deck_id = form.deck.data
        new_card = Cards(question=form.question.data, answer=form.answer.data,deck_id=deck_id)
        db.session.add(new_card)
        db.session.commit()
        return redirect(url_for('html.decks', id=deck_id))

    return render_template("create_card.html", form=form)

@html_bp.route('/card/edit/<int:id>', methods=['GET', 'POST'])
def edit_card(id):
    stmt = db.select(Cards).where(Cards.id == id)
    card = db.session.execute(stmt).scalar()
    form = EditCardForm(obj=card)
    if form.validate_on_submit():
        card.question = form.question.data
        card.answer   = form.answer.data
        db.session.commit()
        return redirect(url_for('html.decks', id=card.deck_id))

    return render_template('edit_card.html', form=form, card=card)

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