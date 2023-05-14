n = int(input("Введите число N: "))

for i in range(2, n+1, 2):
    print(i, end=" ")
    if i % 10 == 0:
        print()
