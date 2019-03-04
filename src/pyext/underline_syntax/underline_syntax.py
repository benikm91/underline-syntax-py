class LazyOperations:

    def __init__(self, operations):
        self.operations = operations

    def __truediv__(self, other):
        return LazyOperations(self.operations + (lambda x: x / other, ))

    def __floordiv__(self, other):
        return LazyOperations(self.operations + (lambda x: x // other, ))

    def __add__(self, other):
        return LazyOperations(self.operations + (lambda x: x + other, ))

    def __toString__(self):
        return LazyOperations(self.operations + (lambda x: str(x), ))

    def __call__(self, x):
        res = x
        for operation in self.operations:
            res = operation(res)
        return res

    def __getattr__(self, name):
        def delayed_getattr():
            return lambda x: getattr(x, name)
        if name == '__toString__':
            return self.__toString__()
        return LazyOperationsNextCall(self.operations + (delayed_getattr(), ))

    def __getitem__(self, key):
        def delayed_getitem():
            return lambda x: x[key]
        return LazyOperations(self.operations + (delayed_getitem(), ))


class LazyOperationsNextCall(LazyOperations):

    def done(self):
        return LazyOperations(self.operations)

    def __call__(self, *args, **kwargs):
        return LazyOperations(self.operations + (lambda x: x(*args, **kwargs), ))


__ = LazyOperations(tuple())
