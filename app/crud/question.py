from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

import models.question as model
import schemas.question as schema


async def get_db_question(
    question: schema.Question,
    session: AsyncSession,
):
    instance = await session.execute(
        select(model.Question).where(
            model.Question.question_id == question['question_id'])
    )
    return instance.scalars().first()


async def save_question(
    question: schema.Question,
    session: AsyncSession,
):
    db_obj = model.Question(**question)
    session.add(db_obj)
    await session.commit()
    await session.refresh(db_obj)


async def get_last_question(
    session: AsyncSession,
):
    last_question = await session.execute(
        select(model.Question).order_by(model.Question.id.desc())
    )
    return last_question.scalars().first()
