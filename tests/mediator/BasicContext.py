
from tests.mediator.IContext import IContext


class BasicContext(IContext):

    def call(self, val: int):
        return val + 1