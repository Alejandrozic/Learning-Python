from abc import ABCMeta, abstractmethod


class Stack:
    __metaclass__ = ABCMeta

    @abstractmethod
    def push(self, data): pass

    @abstractmethod
    def pop(self): pass

    @abstractmethod
    def peek(self): pass

    @abstractmethod
    def is_full(self): pass

    @abstractmethod
    def is_empty(self): pass

