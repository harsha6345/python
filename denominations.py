import math

value = 8372

fives = value/500
after500 = value % 500
two100 = after500/200
after200 = two100 % 200
hundreds = after200/100
after100 = hundreds % 100
fifties = after100 / 50
after50 = fifties % 50
twenties = after50 / 20
after20 = twenties % 20
tens = after20 / 10
after10 = tens % 10
five = after10 / 5
after5 = five % 5
two = after5 / 2
after2 = two % 2
one = after2 / 1
after1 = one % 1

print("Five hundreds : ", math.floor(fives))
print("Two hundreds : ", math.floor(two100))
print("Hundreds : ", math.floor(hundreds))
print("Fifties : ", math.floor(fifties))
print("Twenties : ", math.floor(twenties))
print("Tens : ", math.floor(tens))
print("Fives : ", math.floor(five))
print("Twos : ", math.floor(two))
print("Ones : ", math.floor(one))
