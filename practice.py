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



