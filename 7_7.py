def sum_of_neighbor(lst):
    result = []
    for i in range(len(lst)):
        if i == 0:
            result.append(lst[i + 1] + lst[-1])
        elif i == len(lst) - 1:
            result.append(lst[i - 1] + lst[0])
        else:
            result.append(lst[i - 1] + lst[i + 1])
    return result


user_input = input("Введите список чисел: ")
lst = list(map(int, user_input.split()))
res = sum_of_neighbor(lst)
print(res)
