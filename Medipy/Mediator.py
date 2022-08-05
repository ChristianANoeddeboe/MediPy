
import sys, inspect

from Medipy.IMediator import IMediator
from Medipy.IRequestHandler import IRequestHandler

class Mediator(IMediator):
    
    services: dict[object.__class__, object] = {}
    __request_handlers = {}

    def __init__(self, services = []):
        for service in services:
            self.services[service.__class__] = service
        

    async def send(self, request: object, cancellation_token=None):
        
        if request is None:
            raise ValueError(request.__class__.__name__)

        request_type = type(request)

        if request_type not in self.__request_handlers:
            new_handler = inspect.getmembers(inspect.getmodule(request), lambda member: inspect.isclass(member) and member.__base__ == IRequestHandler)[0].__getitem__(1)
            args = inspect.signature(new_handler.__init__).parameters
            handler_args = {}
            for arg in args:
                if arg == "self":
                    continue
                test = args[arg]
                class_annotation = test.annotation
                if class_annotation is inspect.Parameter.empty:
                    raise ValueError("No annotation for argument " + arg)
                for serv in self.services:
                    if issubclass(serv, class_annotation) or serv == class_annotation:
                        service = self.services[serv]
                        break
                if service is None:
                    raise ValueError("No service for annotation " + str(class_annotation.__class__))
                handler_args[arg] = service
            handler_instance = new_handler(**handler_args)
            self.__request_handlers[request_type] = handler_instance        

        handler: IRequestHandler = self.__request_handlers.get(request_type) #inspect.getmembers(inspect.getmodule(request), lambda member: inspect.isclass(member) and member.__base__ == IRequestHandler)[0].__getitem__(1)
        print(handler.__class__)
        return await handler.handle(request, cancellation_token)

    async def broadcast(self, request, cancellation_token=None):
        pass

