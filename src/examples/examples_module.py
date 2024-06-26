from nest.core import Module
from .examples_controller import ExamplesController
from .examples_service import ExamplesService


@Module(
    controllers=[ExamplesController],
    providers=[ExamplesService],
    imports=[]
)   
class ExamplesModule:
    pass

    