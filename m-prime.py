def reverse_number(n):
    reversed_number = 0
    while n > 0:
        reversed_number = reversed_number * 10 + n % 10
        n //= 10
    return reversed_number


def prime(number):
    flag = True
    flag2 = True
    flagboth = True
    reverse = reverse_number(number)
    for x in range(number - 1, 1, -1):
        if number % x == 0:
            flag = False
    for x in range(number - 1, 1, -1):
        if reverse % x == 0:
            flag2 = False
    if flag == True and flag2 == True:
        flagboth = True
    else:
        flagboth = False
    return flagboth


print(prime(13))
