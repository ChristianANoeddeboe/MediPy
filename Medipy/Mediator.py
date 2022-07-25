
import sys, inspect

from Medipy.IMediator import IMediator
from Medipy.IRequestHandler import IRequestHandler

class Mediator(IMediator):
    
    services = set()
    __request_handlers = {}

    async def send(self, request: object, cancellation_token=None):
        
        if request is None:
            raise ValueError(request.__class__.__name__)

        request_type = type(request)

        if request_type not in self.__request_handlers:
            new_handler = inspect.getmembers(inspect.getmodule(request), lambda member: inspect.isclass(member) and member.__base__ == IRequestHandler)[0].__getitem__(1)
            self.__request_handlers[request_type] = new_handler()        

        handler: IRequestHandler = self.__request_handlers.get(request_type) #inspect.getmembers(inspect.getmodule(request), lambda member: inspect.isclass(member) and member.__base__ == IRequestHandler)[0].__getitem__(1)
        print(handler.__class__)
        return await handler.handle(request, cancellation_token)

    async def broadcast(self, request, cancellation_token=None):
        pass

