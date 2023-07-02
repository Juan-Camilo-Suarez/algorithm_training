n = int(input())
cube = 0
cost = 0
for i in range(1, n + 1):
    cube += ((2 * i - 1) * (2 * i - 1) * 1)
cost = (2 * n - 1) ** 3 - cube
print(cost)
