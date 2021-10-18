from typing import List


class PyStack(List):
    def __init__(self):
        super().__init__()

    def is_empty(self):
        return len(self) == 0

    def push(self, x):
        self.append(x)
        return self

    def pop(self):
        return super().pop()

    def nth(self, n):
        return self[len(self) - 1 - n]

    def take(self, n):
        return self[len(self) - 1 - n:]

    def top(self):
        return self[-1]

    def insert(self, index, val):
        super().insert(len(self)-index, val)
        return self

    def set_nth(self, index, val):
        self[index] = val
        return self

    def flush(self):
        del self[:]
        return self