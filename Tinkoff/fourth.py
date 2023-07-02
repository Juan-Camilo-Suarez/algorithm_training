iterations = int(input())
for _ in range(iterations):
    start, end = map(int, input().split())
    mul = 1
    for i in range(start, end + 1):
        mul *= i
    suma = sum([int(x) for x in str(mul)])
    if len(str(suma)) == 1:
        print(suma)
    else:
        suma = sum([int(x) for x in str(suma)])
        print(suma)
