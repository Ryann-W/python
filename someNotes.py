# find the largest value
largest_so_far = -1
print('Before', largest_so_far)
for the_sum in [9,41,12,3,74,15]:
    if the_sum > largest_so_far:
        largest_so_far = the_sum
    print(largest_so_far, the_sum)
print('After', largest_so_far)

# find the smallest value

smallest = None
print('Before')

for value in [9,41,12,3,74,15]:
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value
    print(smallest,value)
print('After',smallest)


# counting in a loop

zork = 0
print('Before', zork)
for thing in [9,41,12,3,74,15]:
    zork = zork + 1
    print(zork, thing)
print('After', zork)

# summing in a loop
zork1 = 0
print('Before',zork1)
for thing in [9,41,12,3,74,15]:
    zork1 = zork1 + thing
    print(zork1,thing)
print('After',zork1)

# some comments for the String

fruit = 'banana'
x = len(fruit) # print the quantity of banana
print(x)

for letter in 'apple':
    print(letter)


# any continuous section of a string using a colon operator
# the second number is one beyond the end of the slice-"up to but not including"

s = 'Monty Python'
print(s[0:4])
print(s[6:7])
print(s[6:20])
# some build-in function
greet = '  Hello  Bob   '
zap = greet.lower() 
upperWord = greet.upper()

type(greet) # the type of the object
dir(greet) # the differernt methods that we can do to String

position = s.find('P') # position = 6
position2 = s.find('p') # there no p in s, so posiiton2 will return -1

nstr = greet.replace('Bob','Mike')
nstr2 = greet.replace('o','I')

# Stripping Whitespace
# lstrip() and rstrip() remove whitespace at the left and right
# strip() remove both beginning and ending whitespace

greet.lstrip()
greet.rstrip()
greet.strip()

#Prefixes

line = 'Please have a nice day'
line.startswith('Please')
line.startswith('aa')

# Parsing and Extracting

data = 'From stephin.marquard@uct.ac.za Sat Jan   5  09:14:16 2008'
atops = data.find('@')
sppos = data.find(' ', atops) # this means find the space after 'atops'

host = data[atops+1 : sppos] # will print 'uct.ac.za'

# open file 
# handle = open(filename,mode) -- filename is the name of file 
# mode is 'r' (read), 'w'(write)

fhand = open('mo.txt')
inp = fhand.read()
print(len(inp))
print(inp[:20])

# searching through a file
fhand1 = open('mbox-short.txt')
for line in fhand1:
    line = line.rstrip()
    if line.startswith('Form:'):
        print(line)

# another style for searching through a file

fhand2 = open('mbox-short.txt')
for line in fhand2:
    line = line.rstrip()
    if not line.startswith('Form:'):
        continue
    print(line)

# another 
# counting the lines that including the keywords
fname = input('Enter the file name:')
fhand3 = open(fname)
count = 0
for line in fhand3:
    if line.startswith('Subject:'):
        count = count+1
print('there were', count, 'subjectr line in' , fname)


# for the try and catch to complete the program

fname1 =  input('Enter the file name:')
try:
    fhand4 = open(fname1)
except :
    print('File cannot be opened:', fname1)

count1 = 0
for line in fhand4:
    if line.startswith('Subject:'):
        count1 = count1 + 1
print('there were', count1, 'subjectr line in' , fname1)

# list is index specified in square brackets

# list constants are surrounded by square brackets and the elements in the list are separated by commas
# a list element can be any Python object-even another list
# a list can be empty
l = [1,[5,6],7]
# Strings are 'immutable'- we cannot change the contents of a string- we must make a new string to make any change
# lists are 'mutable'- we can change an element of a list using the index operator
lotto = [2,14,26,41,63]
lotto[2] = 28 # lotto will return [2,14,28,41,63]
# len() tells ys the number of elements of any set or sequence (such as a string...)
# the range funciton returns a list of numbers that range form zero to one less than the parameter

# fro the list method, also can use dir() to lookup
# some of are: append, count, extend, index, insert, pop, remove, reverse, sort
# append in list

stuff = list()
stuff.append('book')
stuff.append(99)

