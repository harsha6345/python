for x in range(1, 11, 1):
    line = ""
    if x % 2 != 0:
        for y in range(1, 11, 1):
            line += str(y) + " "
    else:
        for y in range(10, 0, -1):
            line += str(y) + " "
    print(line)
