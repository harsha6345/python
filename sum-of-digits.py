def sum_digits(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum


def reduce_to_one_digit(n):
    while n > 9:
        n = sum_digits(n)
    return n


n = int(input("Enter a number: "))
print(f"The reduced number is {reduce_to_one_digit(n)}.")
