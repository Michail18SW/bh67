num1 = float(input("Введите 1-е число: "))
op = input("Введите оператор (+, -, *, /): ")
num2 = float(input("Введите 2-е число: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
else:
    print("Неверный оператор :(")
