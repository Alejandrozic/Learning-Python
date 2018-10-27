#!/usr/bin/python

"""
Notes:
    Implementation using @property
"""

class MyClass(object):

    def __init__(self,value):
        self._value = value

    @property
    def var(self):
        """ Get attribute """
        return self._value

    @var.setter
    def var(self,value):
        """ Set attribute """
        self._value = value

    @var.deleter
    def var(self):
        """ Delete attribute """
        self._value = None