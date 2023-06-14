n = int(input("Enter no of numbers : "))
numberlist = []
for x in range(n):
    number = int(input("Enter element "))
    numberlist.append(number)
largest = numberlist[0]
smallest = numberlist[0]

for no in numberlist:
    if no > largest:
        largest = no
    elif no < smallest:
        smallest = no

print("Smallest is ", smallest)
print("Largest is ", largest)
