from sqlalchemy import Column, Integer, String

from core.db import Base, PreBase


class Question(Base, PreBase):
    question_id = Column(Integer)
    question_text = Column(String(200), nullable=False)
    answer_text = Column(String(200), nullable=False)
    created_at = Column(String(200), nullable=False)
