def mul_number(a,b):
    if (b == 1):
        return a
    else:
        return a + mul_number(a, b-1)

def print_num(n):
    print(n)
    if n == 1:
        return
    else:
        print_num(n-1)
