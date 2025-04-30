from typing import Optional
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from db import db

class Cards(db.Model):
    __tablename__ = "cards"
    id: Mapped[int] = mapped_column(primary_key=True)
    deck_id: Mapped[int] = mapped_column(ForeignKey("decks.id"))
    question: Mapped[str] = mapped_column(String(120), unique=True)
    answer: Mapped[str] = mapped_column(String(120), unique=True)
    deck: Mapped["Deck"] = relationship(back_populates="cards")
    
class Deck(db.Model):
    __tablename__ = "decks"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    description: Mapped[str] = mapped_column(String(50))
    cards: Mapped[list["Cards"]] = relationship("Cards", back_populates="deck")
