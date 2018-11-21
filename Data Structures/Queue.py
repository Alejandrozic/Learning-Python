from abc import ABCMeta, abstractmethod


class Queue:
    __metaclass__ = ABCMeta

    @abstractmethod
    def enqueue(self, data): pass

    def dequeue(self): pass

    def peek(self): pass

    def is_empty(self): pass

    def is_full(self): pass
