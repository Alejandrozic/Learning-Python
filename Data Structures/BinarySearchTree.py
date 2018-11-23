from abc import ABCMeta, abstractmethod


class BinarySearchTree:
    __metaclass__ = ABCMeta

    @abstractmethod
    def insert(self, data): pass

    @abstractmethod
    def delete(self, data): pass

    @abstractmethod
    def find(self, data): pass
