
def decimal_to_binary(num):
    bin = ""
    while(num > 0):
        bin = bin + str(divmod(num, 2)[1])
        num = divmod(num, 2)[0]
    return bin[::-1]


def decimal_to_oct(num):
    bin = ""
    while(num > 0):
        bin = bin + str(divmod(num, 8)[1])
        num = divmod(num, 8)[0]
    return bin[::-1]


if __name__ == "__main__":
    print(decimal_to_oct(100))

