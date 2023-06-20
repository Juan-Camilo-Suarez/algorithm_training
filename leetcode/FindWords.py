# https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/
from collections import Counter


def countCharacters(words, chars):
    """
    :type words: List[str]
    :type chars: str
    :rtype: int
    """
    counter = 0
    for word in words:
        for ch in word:
            if word.count(ch) > chars.count(ch):
                break
        else:
            counter += len(word)

    return counter


print(countCharacters(words=["cat", "bt", "hat", "tree"], chars="atach"))
