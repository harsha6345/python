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
print("1. Arithmetic mean is ", avg)
print("2. Geometric mean is ", gm)
print("3. Harmonic mean is ", hm)
