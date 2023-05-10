n = int(input("Введите число n: "))
result = {}
for i in range(n+1):
    name = input(f"Введите имя для {i}-го числа: ")
    email = input(f"Введите email для {i}-го числа: ")
    result[i] = {"name": name, "email": email}
print(result)
