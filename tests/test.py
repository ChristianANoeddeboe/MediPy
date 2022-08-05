import inspect

class parameter():
    def __init__(self, name, type, default=None):
        self.name = name
        self.type = type
        self.default = default

class parameter2():
    def __init__(self):
        self.name = None


class test():

    def __init__(self, not_nice: parameter, nice: parameter2, tester = None):
        self.not_nice = not_nice
        self.nice = nice
        self.test = "test"

    def test_function(self):
        print(self.test)
        print(self.not_nice.name)
        print(self.nice.name)

args = inspect.signature(parameter2.__init__).parameters

services: dict[object.__class__, object] = {}

services[test.__class__] = test("not nice", parameter("nice", str))
services[parameter.__class__] = parameter("tester", int)
services[parameter2.__class__] = parameter2()

print(services)

handler_args = {}

for arg in args:
    if arg == "self":
        continue
    print(arg, args[arg].annotation)
    class_annotation = args[arg].annotation
    if class_annotation is inspect.Parameter.empty:
        raise ValueError("No annotation for argument " + arg)
    if class_annotation not in services:
        raise ValueError("No service for annotation " + class_annotation)
    service = services[class_annotation.__class__]
    handler_args[arg] = service

print(handler_args)
handler_instance = parameter2(**handler_args)
print(handler_instance)
#handler_instance.test_function()