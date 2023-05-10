text = input("Введите текст: ")
result = {}
for letter in text:
    if letter in result:
        result[letter] += 1
    else:
        result[letter] = 1
print(result)