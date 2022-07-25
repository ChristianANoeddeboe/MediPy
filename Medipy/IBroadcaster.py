from abc import ABC, abstractmethod

class IBroadcaster(ABC):

    @abstractmethod
    async def broadcast(self, request, cancellation_token=None):
        pass