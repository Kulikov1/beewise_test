from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class QuestionBase(BaseModel):
    question_id: Optional[int]
    question_text: Optional[str]
    answer_text: Optional[str]
    created_at: Optional[datetime]

    class Config:
        title = 'Класс вопроса'


class Question(QuestionBase):
    id: int

    class Config:
        orm_mode = True
