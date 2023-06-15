
def prime(number):
    flag = True
    for x in range(number - 1, 1, -1):
        if number % x == 0:
            flag = False
    return flag


print(prime(13))
