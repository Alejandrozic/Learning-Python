"""
:return: dict
    format {key}={val}
        sql_query=SELECT a FROM b WHERE condition
        email_to=dl@domain.com
        debug=True
    read config as dictionary from file
    write new edited config dict to file
"""

import os

class ConfigDict(dict):

    def __init__(self,filename):
        self._filename = filename
        try:
            assert os.path.isfile(self._filename),"File not found"
            with open(filename) as fh:
                for line in fh:
                    line = line.rstrip()
                    key, value = line.split('=', 1)
                    dict.__setitem__(self, key, value)
        except AssertionError as error:
            print error

    def __setitem__(self, key, value):
        dict.__setitem__(self,key,value)
        with open(self._filename,"w") as fh:
            for key,val in self.items():
                fh.write('{0}={1}'.format(key,val))