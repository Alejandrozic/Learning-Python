from abc import ABCMeta, abstractmethod


class BinarySearchTree:
    __metaclass__ = ABCMeta

    @abstractmethod
    def insert(self, data): pass

    @abstractmethod
    def delete(self, data): pass

    @abstractmethod
    def traverse(self, data): pass

    @abstractmethod
    def get_min(self, data): pass

    @abstractmethod
    def get_max(self, data): pass
