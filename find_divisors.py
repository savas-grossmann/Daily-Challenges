import math

# Create a function that takes an integer and returns an array
# with all of the integer's divisors(except for 1 and the number itself)
# from smallest to largest. If the number is prime
# return the string '(integer) is prime'


# Brute-Force go trough every possible number
def divisor_dumb(n):
    steps = 0
    divisors = []
    for i in range(2, n):
        steps += 1
        if n % i == 0:
            divisors.append(i)
    if len(divisors) == 0:
        print(n, "is a prime! (Steps needed: ", steps, ")")
    else:
        print(divisors, "(Steps needed: ", steps, ")")


# Doesnt go trough all of the Numbers.
# Divisors can only be as big as the Sqrt of n
def divisor_short(n):
    steps = 0
    divisors = []
    for i in range(2, int(math.sqrt(n))):
        steps += 1
        if n % i == 0:
            divisors.append(i)
            if n / i != i:
                divisors.append(int(n/i))
    if len(divisors) == 0:
        print(n, "is a prime! (Steps needed: ", steps, ")")
    else:
        print(sorted(divisors), "(Steps needed: ", steps, ")")


if __name__ == '__main__':
    n = int(input("Input your number: "))
    divisor_dumb(n)
    divisor_short(n)
