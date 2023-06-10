n = int(input('Введите количество чисел: '))
sum = 0
for i in range(n):
    x = float(input(f"Введите {i + 1}-ое число: "))
    sum += x
average = sum/n
print('Среднее арифметическое введённых чисел:', average)
