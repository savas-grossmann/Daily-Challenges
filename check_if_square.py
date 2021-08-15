import math
from random import randint


def check_if_square(num):
    if num < 0:
        return False
    elif num == 0:
        return True
    else:
        return num % math.sqrt(num) == 0


if __name__ == '__main__':
    for i in range(10):
        n = randint(-1, 99999)
        print(n, check_if_square(n))
