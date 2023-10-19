import json

from aiohttp import ClientSession
from sqlalchemy.ext.asyncio import AsyncSession


async def get_question(
    session: AsyncSession,
) -> dict:
    async with ClientSession() as session:
        url = 'https://jservice.io/api/random'
        async with session.get(url=url) as response:
            data = await response.read()
            data_json = json.loads(data)
            question = {
                'question_id': int(data_json[0]['id']),
                'question_text': data_json[0]['question'],
                'answer_text': data_json[0]['answer'],
                'created_at': data_json[0]['created_at'],
            }
        return question
