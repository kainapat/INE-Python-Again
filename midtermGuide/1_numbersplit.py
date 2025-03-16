def numbersplit(num):
    n = num // 2
    return [n, num - n]

print(numbersplit(4))
print(numbersplit(10))
print(numbersplit(11))
print(numbersplit(-9))

