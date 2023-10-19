from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.db import get_async_session
from crud.question import get_db_question, get_last_question, save_question
from schemas.question import QuestionBase
from service.get_questions import get_question

router = APIRouter()

empty_body = {
        'question_id': None,
        'question_text': None,
        'answer_text': None,
        'created_at': None,
    }


@router.post(
    '/',
    response_model=QuestionBase,
)
async def greetings(
    questions_num: int,
    session: AsyncSession = Depends(get_async_session),
):
    while questions_num > 0:
        new_question = await get_question(session)
        db_question = await get_db_question(new_question, session)
        if db_question:
            pass
        else:
            await save_question(new_question, session)
            questions_num -= 1
    question = await get_last_question(session)
    if question:
        return question
    return empty_body
