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

# the get method for dictionaries

number = dict()
names2 = ['aaa','aaa','ccc','ccc','vvv','vvv','bbb','ddd','bbb','vvv']

for name in names2:
    number[name] = number.get(name,0)+1
print(number)

print(number.get('xxx',90))
# some comments from above, if the parameter in the dict, the default value u put in the get cannot be changed, when u print it , it will return the value in dict
# if the parameter is not in the dict, it will print the value u put in the get function

# counting pattern -- counting words

countss = dict()
print('Enter a line of text: ')
line = input('')

words = line.split()

print('words:', words)

for word in words:
    countss[word] = countss.get(word,0)+1

print(countss)
print('Counts', countss)

# print the dictionaries

aaa  = {'r':21,'e':45,'v':45,'f':67,'c':34}

for bbb in aaa:
    print(bbb,aaa[bbb])

#Retrieving lists of Keys and Values

print(aaa.keys())
print(aaa.values())
print(aaa.items())

for ccc,ddd in aaa.items():
    print(ccc,ddd)

# this is an example that open a file, and counting words, finally print the most frequent words

name = input('open file:')
handle = open(name)

counts2 = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts2[word] = counts2.get(word,0) + 1

bigcount = None
bigword = None
for word, countsss in counts2.items():
    if bigcount is None or countsss > bigcount:
        bigcount = countsss
        bigword = word

print(bigword,bigcount)

Sneak peek 先睹为快
