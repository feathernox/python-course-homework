# Stack.

import sys


class Stack(object):
    def __init__(self, elements):
        self.stack = list(elements)

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        self.stack.pop()

    def top(self):
        return self.stack[-1]

    def __len__(self):
        return len(self.stack)

    def __str__(self):
        return " ".join(map(str, self.stack))

exec(sys.stdin.read())
