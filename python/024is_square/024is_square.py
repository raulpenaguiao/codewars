from math import sqrt, floor
def is_square(n):
    if n <= 0:
        return n == 0
    print(n)
    return n == floor(sqrt(n))**2
