from typing import Optional
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from db import db

class Deck(db.Model):
    __tablename__ = "decks"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    description: Mapped[str] = mapped_column(String(50))
    cards: Mapped[list["Cards"]] = relationship("Cards", back_populates="deck")
