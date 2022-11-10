import operator


class Calculator:
    """A calculator with a storage for variables."""

    def __init__(self):
        self.last_result = 0
        self.memory = {}

    def _compute(self, x, y, op):
        if isinstance(x, str):
            x = self.memory.get(x, 0)
        if isinstance(y, str):
            y = self.memory.get(y, 0)
        self.last_result = op(x, y)
        return self.last_result

    def add(self, x, y):
        return self._compute(x, y, operator.add)

    def sub(self, x, y):
        return self._compute(x, y, operator.sub)

    def mul(self, x, y):
        return self._compute(x, y, operator.mul)

    def div(self, x, y):
        return self._compute(x, y, operator.truediv)

    def pow(self, x, y):
        return self._compute(x, y, operator.pow)

    def store(self, name):
        self.memory[name] = self.last_result
