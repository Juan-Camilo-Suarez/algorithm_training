iterations = int(input())
queue = []
duplicated_list = []
for _ in range(iterations):
    values = input().split()
    start = int(values[0])

    if start == 1:
        end = int(values[1])
        queue.append(end)
    elif start == 2:
        duplicated_list = []
        for number in queue:
            duplicated_list.extend([number, number])
        queue = duplicated_list
    elif start == 3:
        removed_element = queue.pop(0)
        print(removed_element)