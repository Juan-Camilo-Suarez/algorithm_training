# https://leetcode.com/problems/top-k-frequent-elements/
def topKFrequent(nums, k):
    mydict = {}
    for i in nums:
        mydict[i] = mydict.get(i, 0) + 1

    sorted_items = sorted(mydict.items(), key=lambda x: x[1], reverse=True)
    top_k_keys = [x[0] for x in sorted_items[:k]]

    return top_k_keys


print(topKFrequent([1, 1, 1, 2, 2, 3], 2))
