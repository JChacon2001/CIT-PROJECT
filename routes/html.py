from flask import Blueprint, render_template, redirect, url_for
from flask import session, request
from models import *
from forms import DeckForm, CardForm, EditCardForm, csvForm, StudyForm
from db import db
from sqlalchemy import func, case, update
import csv,io
html_bp = Blueprint("html", __name__)

@html_bp.route("/")
def home():
    results = (
    db.session.query(
        Deck.id,
        Deck.name,
        Deck.upload_date,
        Deck.last_studied,
        func.count(Cards.id).label("total"),
        func.count(case((Cards.completed == True, 1))).label("completed")
    )
    .outerjoin(Cards) 
    .group_by(Deck.id)
    .all()
    )
    deck_data = []
    for deck_id, name, upload_date, last_studied, total, completed in results:
        percent = round((completed / total) * 100) if total > 0 else 0
        deck_data.append({
            "id":deck_id,
            "name": name,
            "upload_date": upload_date,
            "total": total,
            "completed": completed,
            "percent": percent,
            "last_studied":last_studied
        })


    top4 = db.session.execute(db.select(Deck).limit(4)).scalars()
    return render_template("home.html", top4=top4, Deck=deck_data)

@html_bp.route("/qa")
def q_and_a():
    return render_template("QA.html")

@html_bp.route("/decks")
def decks():
    results = (
        db.session.query(
            Deck.id,
            Deck.name,
            Deck.upload_date,
            Deck.last_studied,
            func.count(Cards.id).label("total"),
            func.count(case((Cards.completed == True, 1))).label("completed")
        )
        .outerjoin(Cards, Deck.id == Cards.deck_id)
        .group_by(Deck.id, Deck.name, Deck.upload_date, Deck.last_studied)
        .all()
    )

    deck_data = []
    for deck_id, name, upload_date, last_studied, total, completed in results:
        percent = round((completed / total) * 100) if total > 0 else 0
        deck_data.append({
            "id": deck_id,
            "name": name,
            "upload_date": upload_date,
            "total": total,
            "completed": completed,
            "percent": percent,
            "last_studied": last_studied
        })

    return render_template("alldecks.html", data=deck_data)

@html_bp.route("/decks/<int:id>")
def deckcont(id):
    stmt = db.select(Cards).where(Cards.deck_id == id)
    exec = db.session.execute(stmt).scalars().all()
    return render_template("deck.html", data=exec)

@html_bp.route("/deck/new", methods=['GET', 'POST'])
def deck_form():
    form = DeckForm()
    if form.validate_on_submit():
        cat_name = form.category.data

        stmt = db.select(Category).where(Category.name == cat_name)
        category = db.session.execute(stmt).scalar()
        
        if category is None:
            category = Category(name=cat_name)
            db.session.add(category)
            db.session.commit()  # Commit so we have category.id

        new_deck = Deck(
            name=form.name.data,
            description=form.description.data,
            category_id=category.id  # 🔗 Link here!
        )
        db.session.add(new_deck)
        db.session.commit()

        return redirect(url_for("html.decks"))

    return render_template("create_deck.html", form=form)

@html_bp.route('/card/new', methods=['GET', 'POST'])
def create_card():
    form = CardForm()
    stmt = db.select(Deck   ).order_by(Deck.name)
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

@html_bp.route('/deck/edit/<int:id>', methods=['GET', 'POST'])
def edit_deck(id):
    stmt = db.select(Deck).where(Deck.id == id)
    deck = db.session.execute(stmt).scalar()
    form = DeckForm(obj=deck)
    if request.method == "GET" and deck.category:
        form.category.data = deck.category.name
    if form.validate_on_submit():
        deck.name = form.name.data
        deck.description   = form.description.data
        cat_name = form.category.data
        stmt = db.select(Category).where(Category.name == cat_name)
        category = db.session.execute(stmt).scalar()
        if category is None:
            category = Category(name=cat_name)
            db.session.add(category)
        deck.category = category
        db.session.commit()
        return redirect(url_for('html.decks', id=id))
    return render_template('edit_deck.html', form=form, deck=deck)

@html_bp.route('/card/delete/<int:id>')
def delete_card(id):
    stmt = db.select(Cards).where(Cards.id == id)
    card = db.session.execute(stmt).scalar()
    stmt2 = db.session.execute(db.select(Deck).where(Deck.id == card.deck_id)).scalar()
    r2 = stmt2.id
    db.session.delete(card)
    db.session.commit()
    return redirect(url_for('html.deckcont', id=r2))

@html_bp.route('/deck/delete/<int:id>')
def delete_deck(id):
    stmt = db.select(Deck).where(Deck.id == id)
    deck = db.session.execute(stmt).scalar()
    if deck:
        for cards in deck.cards:
            db.session.delete(cards)
        db.session.delete(deck)
        db.session.commit()
    return redirect(url_for('html.decks'))


@html_bp.route("/import", methods=["GET", "POST"])
def import_csv():
    data = []
    form = csvForm()
    decks = db.session.execute(db.select(Deck)).scalars()
    msg  = request.args.get("msg", "")
    form.deck.choices = [(d.id, d.name) for d in decks]
    if form.validate_on_submit():
        deck = db.session.execute(db.select(Deck).where(Deck.id == form.deck.data)).scalar()
        f = form.csv.data
        reader = csv.DictReader(io.StringIO(f.read().decode("utf-8")))
        for r in reader:
            q = r["question"]
            a = r["answer"]
            db.session.add(Cards(deck_id=deck.id, question=q, answer=a))
            data.append({"deck": deck.name, "question": q, "answer": a})
        db.session.commit() 
        msg = f"Imported {len(data)} cards into “{deck.name}”"
        return render_template("import.html",form=form,data=data,msg=msg)
    return render_template("import.html", form=form,data=data,msg=msg)

from flask import redirect, url_for

@html_bp.route("/study/<int:id>", methods=["GET", "POST"])
def study_deck(id):
    form = StudyForm()

    stmt = db.session.execute(
        db.select(Cards).where(Cards.deck_id == id, Cards.completed == False)
    ).scalars()
    result = list(stmt)
    total_cards = len(result)

    if total_cards == 0:
        return render_template("congrats.html", redirect_url=url_for("html.decks"))

    db.session.execute(
        update(Deck).where(Deck.id == id).values(last_studied=func.now())
    )
    db.session.commit()

    if form.validate_on_submit():
        current_index = int(form.card_index.data)

        if form.previous.data:
            current_index = (current_index - 1) % total_cards

        elif form.studied.data:
            current_card = result[current_index]
            current_card.completed = True
            db.session.commit()  

            stmt = db.session.execute(
                db.select(Cards).where(Cards.deck_id == id, Cards.completed == False)
            ).scalars()
            result = list(stmt)
            total_cards = len(result)

            if total_cards == 0:
                return render_template("congrats.html", redirect_url=url_for("html.decks"))

            current_index = 0

        elif form.next.data:
            current_index = (current_index + 1) % total_cards

    else:
        current_index = 0

    form.card_index.data = str(current_index)
    current_card = result[current_index]

    return render_template(
        "study.html",
        form=form,
        card=current_card,
        current_index=current_index,
        total_cards=total_cards
    )


@html_bp.route("/faq")
def faq():
    return render_template("faq.html")

@html_bp.route("/testcard")
def testcard():
    if "card_index" not in session:
        session["card_index"] = 0

    all_cards = db.session.execute(db.select(Cards)).scalars().all()

    if not all_cards:
        return "No cards available."

    index = session["card_index"] % len(all_cards)
    current_card = all_cards[index]

    return render_template("testcard.html", question=current_card.question, answer=current_card.answer)

@html_bp.route("/testcard/next", methods=["POST"])
def next_testcard():
    session["card_index"] = session.get("card_index", 0) + 1
    return redirect(url_for("html.testcard"))

@html_bp.route("/testcard/back", methods=["POST"])
def back_testcard():
    if not session["card_index"] == 0 or not session["card_index"] < 0:
        session["card_index"] = session.get("card_index",0) - 1
    return redirect(url_for("html.testcard"))

@html_bp.route("/Acards")
def allcards():
    cards = db.session.execute(db.select(Cards)).scalars()
    return render_template("allcards.html", data=cards)

@html_bp.route("/courses")
def courses():
    res = db.session.execute(db.select(Category)).scalars()
    return render_template("courses.html", data=res)


@html_bp.route("/deck/<int:id>/reset", methods=["POST"])
def reset_completion(id):
    db.session.query(Cards).filter(Cards.deck_id == id).update({Cards.completed: False})
    db.session.commit()
    return redirect(url_for("html.decks"))