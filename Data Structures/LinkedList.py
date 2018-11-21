from abc import ABCMeta, abstractmethod


class LinkedList:
    __metaclass__ = ABCMeta

    @abstractmethod
    def append(self, data): pass

    @abstractmethod
    def prepend(self, data): pass

    @abstractmethod
    def delete(self, data): pass

    @abstractmethod
    def get_nodes(self): pass

    @abstractmethod
    def get_size(self): pass
