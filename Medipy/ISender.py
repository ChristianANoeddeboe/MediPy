from abc import ABC, abstractmethod

class ISender(ABC):

    @abstractmethod
    async def send(self, request, cancellation_token=None):
        pass