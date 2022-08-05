

from Medipy.IRequestHandler import IRequestHandler
from tests.mediator.IContext import IContext



class TestCommand():

    id: int
    title: str = None

class TestCommandHandler(IRequestHandler[TestCommand, bool]):

    __context: IContext

    def __init__(self, context: IContext):
        self.__context = context

    async def handle(self, request: TestCommand, cancellation_token=None) -> int:
        res = self.__context.call(request.id)
        return res
