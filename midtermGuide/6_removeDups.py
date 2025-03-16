def removeDups(arr):
    return list(dict.fromkeys(arr))


print(removeDups([1, 0, 1, 0]))
print(removeDups(["The", "big", "cat"]))
print(removeDups(["John", "Taylor", "John"]))
