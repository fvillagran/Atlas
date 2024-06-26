from nest.core import Controller, Get, Post, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.config import config


from .examples_service import ExamplesService
from .examples_model import Examples


@Controller("examples")
class ExamplesController:

    def __init__(self, examples_service: ExamplesService):
        self.examples_service = examples_service

    @Get("/")
    async def get_examples(self, session: AsyncSession = Depends(config.get_db)):
        return await self.examples_service.get_examples(session)

    @Post("/")
    async def add_examples(self, examples: Examples, session: AsyncSession = Depends(config.get_db)):
        return await self.examples_service.add_examples(examples, session)
 