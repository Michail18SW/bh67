def reverse_string(st):
    if len(st) == 0:
        return st
    else:
        return reverse_string(st[1:]) + st[0]


s = input("Введите строку: ")
print(f'Обратная строка: {reverse_string(s)}')
