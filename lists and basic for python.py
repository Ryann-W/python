# continue with list in python

# append in list
stuff = list()
stuff.append('book')
stuff.append(99)
# stuff will retun ['book',99]
# something in a list ?
some = [4,5,6,7,8,9]

9 in some # will return true
10 in some # will return False
15 not in some # will retun true

# the sort method, a list can be sorted

friends = ['Franklin','Sally','Glenn']
friends.sort()

print(friends) # will return ['Franklin','Glenn','Sally'] , already be sorted

# some built-in functions in lists
nums = [2,41,12,9,74,15]
print(len(nums))  # the numbers of nums
print(max(nums)) # the max value
print(min(nums)) # the min value
print(sum(nums)) # the sum of the nums
print(sum(nums) / len(nums)) # the average of nums

# here are two examples for input numbers and average them 

total = 0
count = 0
while True:
    inp = input('enter a numer: ')
    if inp == 'done':
        break
    value = float(inp)
    total = total + value
    count = count + 1

average = total / count # with out list

# within list

numlist = list()
while True:
    inp1 = input('enter a value: ')
    if inp1 == 'done':
        break
    value = float(inp1)
    numlist.append(value)

average = sum(numlist) / len(numlist)

