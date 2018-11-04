"""
:return: dict
    Format key=val or key=v1,v2,v3,...
    Read config file to dict
"""

import os


class ConfigDict(dict):

    def __init__(self, filename):
        self._filename = filename
        try:
            assert os.path.isfile(self._filename), "ConfigDict:: File {0} not found".format(self._filename)
            with open(self._filename) as fh:
                for line in fh:
                    line = line.rstrip()
                    key, value = line.split('=', 1)
                    if len(value.split(',')) > 1:
                        value = value.split(',')
                    dict.__setitem__(self, key, value)

        except AssertionError as error:
            print error

    def __setitem__(self, key, value):
        dict.__setitem__(self, key, value)
        with open(self._filename, "w") as fh:
            for key, val in self.items():
                fh.write('{0}={1}'.format(key, val))
