from typing import Optional
from sqlalchemy import String, ForeignKey, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from db import db

class Deck(db.Model):
    __tablename__ = "decks"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    description: Mapped[str] = mapped_column(String(50), nullable=True)
    cards: Mapped[list["Cards"]] = relationship("Cards", back_populates="deck")
    upload_date: Mapped[str] = mapped_column(DateTime, default=func.now())
    last_studied: Mapped[str] = mapped_column(DateTime, nullable=True)
    category_id: Mapped[int]    = mapped_column(ForeignKey("categories.id"), nullable=True)
    category:    Mapped["Category"] = relationship("Category", back_populates="decks")