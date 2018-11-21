"""
    Circular Queue Implementation (Integers)
"""
from Queue import Queue


class MyCircularQueue(Queue):

    def __init__(self, size):
        self.queue = []
        self.size = size
        self.head = 0
        self.tail = 0

    def enqueue(self, num):
        pass

    def dequeue(self):
        pass

    def peek(self):
        return self.queue[self.head]

    def is_empty(self):
        if len(self.queue) <= 0:
            return True
        return False

    def is_full(self):
        if len(self.queue) > 0:
            return True
        return False
