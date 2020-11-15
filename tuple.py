# tuples are another kind of sequence that functions much like a list,
# they have elements which are indexed starting at 0
# !!! tuples are "immutable"!!! 
a = list()
print(dir(a))
# 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'
b = tuple()
print(dir(b))
# 'count', 'index'

# when we making "temporary variables" we prefer tuples over lists
(x,y) = (4,'fred')
(c,d) = (99,100)
print(x)
print(d)

# the items() method in dictionaries returns a list of (key,values)tuples

# the comparison operators work with tuples and other sequences. IF the first item is equal, Python goes on to the next element, and so on, 
#until it finds elements thst differ.

# sorting list of tuples

a = {}
a['b'] = 1
a['a'] = 2
a['s'] = 3
a['m'] = 4
print(a)

print(sorted(a.items()))

c = {'a':10, 'b':1, 'c':22}
tmp = list()
for k,v in c.items():
    tmp.append((v,k))

new = sorted(tmp, reverse=True)

# if without reverse = True, it will sorted form smaller value to larger value

print(new)

# the top ten most common words from a txt file

fhand  = open('remote.txt') # open the file
counts = dict() # create a dict for counting 

for lines in fhand:
    words = lines.split() # split the lines to a list
    for word in words:
        counts[word] = counts.get(word,0) + 1 # setup the dict


lst = list() #create a new list to save the items of counts, make it to a list of tuples

for key ,value in counts.items():
    lst.append((value,key))

newList = sorted(lst, reverse=True)

for value, key in newList[:10]:
    print(key, value)



cc = {'a':10,'b':1,'c':22}

print( sorted( [ (v,k) for k,v in c.items() ] , reverse=True) )
