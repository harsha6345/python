n = int(input("No of numbers : "))
numberarr = []
for i in range(n):
    x = int(input("Enter number "))
    numberarr.append(x)
sum = 0
for i in range(n):
    sum += numberarr[i]
multiply = 1
for i in range(n):
    multiply *= numberarr[i]

gm = multiply ** (1 / n)
denom = 0
for i in range(n):
    denom += 1/numberarr[i]

hm = n / denom

avg = sum / n
print("The Arithmetic mean is ", avg)
print("Geometric mean is ", gm)
print("Harmonic mean is ", hm)
