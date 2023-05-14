lst = [1, 2, 3, 4, 5, 6]
lst = sorted(lst, key=lambda x: x % 2 != 0)
print(lst)
