n = int(input("No of numbers : "))
numberarr = []
for i in range(n):
    x = int(input("Enter number "))
    numberarr.append(x)
sum = 0
for i in range(n):
    sum += numberarr[i]
avg = sum / n
print("The average is ", avg)
