def is_happy_number(n):
    while True:
        digit_squares_sum = 0
        while n > 0:
            digit = n % 10
            digit_squares_sum += digit * digit
            n //= 10
        if digit_squares_sum == 1:
            return True
        elif digit_squares_sum == 4:
            return False
        else:
            n = digit_squares_sum


number = int(input("Enter a number: "))
if is_happy_number(number):
    print(number, "is a happy number!")
else:
    print(number, "is an unhappy number!")
