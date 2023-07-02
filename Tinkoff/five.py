iterations = int(input())
my_string = ''
char_counts = {}

for _ in range(iterations):
    n = input()
    my_string += n

for char in my_string:
    if char in char_counts:
        char_counts[char] += 1
    else:
        char_counts[char] = 1

ugly = max(char_counts.values()) - min(char_counts.values())
strong = sum(char_counts.values())
print(strong - ugly)
