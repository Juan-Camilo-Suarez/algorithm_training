# https://leetcode.com/problems/first-unique-character-in-a-string/
from collections import Counter


# el primer caracter que no se repita
def firstUniqChar(self, s):
    freq = Counter(s)

    for e in s:
        if freq[e] == 1:
            return s.index(e)

    return -1
