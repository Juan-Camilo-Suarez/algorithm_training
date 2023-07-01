# https://leetcode.com/problems/longest-common-prefix/

def longestCommonPrefix(strs):
    if len(strs) == 0:
        return ""
    current = strs[0]
    for i in strs:
        while not i.startswith(current):
            current = current[:-1]

    return current


print(longestCommonPrefix(strs=["flower", "flow", "flight"]))
