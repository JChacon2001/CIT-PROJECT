from typing import Optional
from sqlalchemy import String, ForeignKey, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from db import db

class Cards(db.Model):
    __tablename__ = "cards"
    id: Mapped[int] = mapped_column(primary_key=True)
    deck_id: Mapped[int] = mapped_column(ForeignKey("decks.id"))
    question: Mapped[str] = mapped_column(String(120))
    answer: Mapped[str] = mapped_column(String(120))
    created: Mapped[str] = mapped_column(DateTime, default=func.now())
    deck: Mapped["Deck"] = relationship("Deck", back_populates="cards")
    
    