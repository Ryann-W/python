# the Dictionary of python
# these definition originally from FreeCodeCamp
# what is collection
# A collection is nice because we can put more than one vlaue in it and canrry them all around in one convinent package
# We have a bunch of values in a single'variable'
# We do this by having more than one place'in' the variable
# We have ways of finding the different places in the variables


# List == A linear collection of values that stay in order
# Dictionary == A 'bag' of values, each with its own label

# lists index their entries based on the position in the list
# Dict are like bags , no order, so we index the things we put in the dictionary with a 'look up bag'

purse = dict() # setup a blank dict
purse['Money'] = 10
purse['candy'] = 3
purse['tissues'] = 75
print(purse) # it will return {'Money': 10, 'candy': 3, 'tissues': 75}
purse['candy']  = purse['candy'] + 2
print(purse) # {'Money': 10, 'candy': 5, 'tissues': 75}

# the comparision of Lists and Dictionaries
# list
list = list()
list.append(1)
list.append(2)
list.append(3)

# dict
dict1 = dict()
dict1['age'] = 12
dict1['course']  = 182

print(list) # return [1, 2, 3]
print(dict1) # return {'age': 12, 'course': 182}

#          list                      Dict
#  key            value     key              value 
#  [0]               1       age                12
#  [1]               2       course             182

# make an empty dictionary using empty curly braces
pp = { }
bb = {'a':1, 'b':2, 'c':3}
print(type(pp))
print(dir(pp))

# Dictionary Tracebacks

bb = dict()

#'cese' in bbb 
# true indicates 'cese' in bbb, flase indicates 'cese' not in bbb

# counting names, if the name repeat , the value add 1 otherwise, value is 1

counts = dict()
names = ['aaa','bbb','aaa','bbb','ccc','eee','fff']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
print(counts)