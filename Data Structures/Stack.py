from abc import ABCMeta, abstractmethod


class Stack:
    __metaclass__ = ABCMeta

    @abstractmethod
    def push(self, data): pass

    def pop(self): pass

    def peek(self): pass

    def get_size(self): pass

    def is_full(self): pass

    def is_empty(self): pass

