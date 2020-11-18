# the practice in py4e.com

# here is the question

#5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. 
# Once 'done' is entered, print out the largest and smallest of the numbers. 
# If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. 
# Enter 7, 2, bob, 10, and 4 and match the output below.
'''
largest = None
smallest = None
lst = list()
while True:
    try:
        num = input("Enter a number: ")
        if num == "done" : break
        num = int(num)
        lst.append(num)
    except ValueError:
        print("Invalid input")
        
for a in lst:
    if largest is None or a > largest:
        largest = a

        
for b in lst:
    if smallest is None or b < smallest:
        smallest = b
   
print("Maximum is ", largest)	
print("Minimum is ", smallest)

tot = 0
sum = 0
for i in [5, 4, 3, 2, 1] :
    tot = tot + 1
    sum = sum + i
print(tot)
print(sum)

# the find() method is find the position in a string , position means index in a string 


for letter in 'banana' :
    print(letter)




# 7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. 
# Do not use the sum() function or a variable named sum in your solution.
# You can download the sample data at http://www.py4e.com/code3/mbox-short.txt 
# when you are testing below enter mbox-short.txt as the file name.



fname = input("Enter file name: ")
fh = open(fname)
total = 0
count = 0
middle = list()
final = list()
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        print(line)
        middle = line.split()
        final.append(float(middle[1]))

for value in final:
    total = total + value
    count = count + 1

average = total / count
print("Average spam confidence:",average)

print("Done")


#8.4 Open the file romeo.txt and read it line by line. 
# For each line, split the line into a list of words using the split() method. 
# The program should build a list of words. 
# For each word on each line check to see if the word is already in the list and if not append it to the list. 
# When the program completes, sort and print the resulting words in alphabetical order.
# You can download the sample data at http://www.py4e.com/code3/romeo.txt

fname = input("Enter a file name:")
fhand = open(fname)
lst = list()

count = 0
for line in fhand:
    line.split()
    for item in line.split():
        lst.append(item)

print(list(set(sorted(lst))))
    



# fname = input("Enter file name: ")
# if len(fname) < 1 : fname = "mbox-short.txt"

fh = open("mbox-short.txt")
count = 0
odd = 0
for line in fh:
    odd = odd + 1
    if(line.startswith("From")) and (odd % 2 == 0):
        print(line.split()[1])
        count = count + 1

print("There were", count, "lines in the file with From as the first word")

'''

handle = open("mbox-short.txt")
count = 0
odd = 0
value = 0
lst = list()
dt = dict()
dt2 = dict()
dt3 =dict()
for line in handle:
    odd = odd + 1
    if(line.startswith("From")) and (odd % 2 == 0):
        print(line.split()[1])
        lst.append(line.split()[1])

print(lst)

for key in lst:
    dt[key] = dt.get(key,0) + 1

print("method1: ",dt)

for key in lst:
    if key not in dt2: # if the key is not in dictionaries, set the value to 1
        dt2[key] = 1
    else:
        dt2[key] = dt2[key] + 1
    
print("method2: ",dt2)

for item,value in dt.items():
   print("converse the dic: ",(value,item))
   dt3[value] = item

# for reverse the key and value in a dict , another shorter method:

dt33 = [(value,key) for key,value in dt.items()] # it returns a touple list not a dict



print(max(dt3.items())[1],max(dt3))

print("------------------")
print("reverse a dict using for loop: ",dt3)
print("more efficient method: ", dt33)
print("---------------------")
