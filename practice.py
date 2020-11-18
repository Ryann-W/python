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


'''

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
print(average)

print("Done")

