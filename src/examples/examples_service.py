from .examples_model import Examples
from .examples_entity import Examples as ExamplesEntity
from nest.core.decorators.database import async_db_request_handler
from nest.core import Injectable

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

@Injectable
class ExamplesService:

    @async_db_request_handler
    async def add_examples(self, examples: Examples, session: AsyncSession):
        new_examples = ExamplesEntity(
            **examples.dict()
        )
        session.add(new_examples)
        await session.commit()
        return new_examples.id

    @async_db_request_handler
    async def get_examples(self, session: AsyncSession):
        query = select(ExamplesEntity)
        result = await session.execute(query)
        return result.scalars().all()
