"""
    File for notes
"""
import pickle
import re


##################################
# Pickle for data Serialization  #
##################################

myList = ['a', 'b', 'c', 'd']

with open('datafile.pickle', 'w') as fh:
    pickle.dump(myList, fh)

with open('datafile.pickle') as fh:
    unpickledlist = pickle.load(fh)


##########
# Regex  #
##########

regex = re.compile('(?P<nums>[\d]+)(?P<none_nums>[\D]+)')

match = regex.search('1234abc 567')

print match.groupdict()             # {'letters': 'abc', 'none_nums': '1234'}
print match.groups()                # ('1234', 'abc')
print match.group('nums')           # 1234
print match.group('none_nums')      # abc
print match.group(0)                # 1234abc
print match.group(1)                # 1234
print match.group(2)                # abc


###################
# Format Strings  #
###################

print '{0} {1} {vehicle}'.format(0, 1, vehicle='car')   # 0 1 car
# with r'' escapes won't be translated
print r'a\nb'                                           # a\nb

############
#  Lambda  #
############

[attr for attr in dir({}) if '__' not in attr]
# Prints
# ['clear', 'copy', 'fromkeys', 'get', 'has_key',
# 'items', 'iteritems', 'iterkeys', 'itervalues',
# 'keys', 'pop', 'popitem', 'setdefault', 'update',
# 'values', 'viewitems', 'viewkeys', 'viewvalues']
