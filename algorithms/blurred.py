"""
Solution for task
http://codeforces.com/gym/102465/problem/B
"""
from pprint import pprint

size = int(input())
matrix = []

for i in range(size):
    start, end = map(int, input().strip().split())
    matrix.append([int(start <= i <= end) for i in range(size)])
    print('added', '{:^6}'.format(i), '\r', end='')

# pprint(matrix)

maximum = 0
for i in range(size):
    print('current i:', i, '\r', end='')
    for j in range(size):
        current = matrix[i][j]
        upper = matrix[i - 1][j] if i - 1 >= 0 else 0
        diag = matrix[i - 1][j - 1] if i - 1 >= 0 and j - 1 >= 0 else 0
        left = matrix[i][j - 1] if j - 1 >= 0 else 0
        matrix[i][j] = current + min(upper, diag, left)
        maximum = max(maximum, matrix[i][j])

# pprint(matrix)
print('overall max:', maximum)
