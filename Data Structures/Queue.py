from abc import ABCMeta, abstractmethod


class Queue:
    __metaclass__ = ABCMeta

    @abstractmethod
    def enqueue(self, data): pass

    @abstractmethod
    def dequeue(self): pass

    @abstractmethod
    def peek(self): pass

    @abstractmethod
    def is_empty(self): pass

    @abstractmethod
    def is_full(self): pass
