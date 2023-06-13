for x in range(1, 11, 1):
    line = ""
    if x % 2 != 0:
        for y in range(1, 11, 1):
            if y % 2 != 0:
                line += str(y) + " "
            else:
                line += "  "
        print(line)
    else:
        print()
