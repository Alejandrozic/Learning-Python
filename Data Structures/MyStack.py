"""
    Array of Integers Implementation
"""

from Stack import Stack


class MyStack(Stack):

    def __init__(self, size):
        self.stack = []
        self.size = size
        self.top = 0

    def push(self, n):
        # O(1) Time Complexity
        if not self.is_full():
            self.stack.append(n)
            self.top += 1

    def pop(self):
        # O(1) Time Complexity
        if not self.is_empty():
            self.top -= 1
            value = self.stack.pop(self.top)
            return value

    def peek(self):
        # O(1) Time Complexity
        return self.stack[self.top]

    def is_empty(self):
        if len(self.stack) <= 0:
            return True
        return False

    def is_full(self):
        if len(self.stack) == self.size:
            return True
        return False

    def get_items(self):
        return self.stack


if __name__ == '__main__':
    ###########
    # Testing #
    ###########

    mystack = MyStack(6)

    # Test Push - Fill Stack
    mystack.push(1)
    mystack.push(2)
    mystack.push(3)
    mystack.push(4)
    mystack.push(5)
    mystack.push(6)

    # Test Push - Attempt overfilling stack
    # items should be ignored
    mystack.push(7)
    mystack.push(8)

    # Test pop
    mystack.pop()

    print mystack.get_items()
