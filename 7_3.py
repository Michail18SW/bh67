lst = [1, 2, 3, 4, 5, 6, 7]
N = int(input('Введите N: '))
lst = lst[-N:] + lst[:-N]
print(lst)
