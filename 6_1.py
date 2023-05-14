n = int(input("Введите число N: "))
m = int(input("Введите число M: "))
k = int(input("Введите число K: "))
result = []
i = 1
while len(result) < n:
    if i % m == 0 and i >= k:
        result.append(i)
    i += 1
print(result)
