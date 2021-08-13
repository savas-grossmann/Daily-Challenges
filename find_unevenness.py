def find_unevenness(numbers):
    even = []
    uneven = []
    numbers = numbers.split()
    for n in numbers:
        if int(n) % 2 == 0:
            even.append(n)
        else:
            uneven.append(n)
    return numbers.index(even[0]) + 1 if len(even) < len(uneven) else numbers.index(uneven[0]) + 1


if __name__ == '__main__':
    print(3 == find_unevenness("2 4 7 8 10"))
    print(1 == find_unevenness("1 2 2"))