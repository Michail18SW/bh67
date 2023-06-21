def power_range(number, start, end):
    for i in range(start, end + 1):
        yield number ** i


number = 2
start = 3
end = 5
result = list(power_range(number, start, end))
print(result)
