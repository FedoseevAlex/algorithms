number = int(input())
result = list()
n = 1

while number != 0:
    if number > 2 * n:
        result.append(n)
        number -= n
    else:
        result.append(number)
        number = 0
    n += 1

print(*result)
