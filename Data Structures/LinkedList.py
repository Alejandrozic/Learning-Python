from abc import ABCMeta, abstractmethod


class LinkedList:
    __metaclass__ = ABCMeta

    @abstractmethod
    def append(self, data): pass

    def prepend(self, data): pass

    def delete(self, data): pass

    def get_nodes(self): pass

    def get_size(self): pass
