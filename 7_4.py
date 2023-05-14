lst = [1, 'hello', 2.5, 'world', True, 'python']
lst = list(filter(lambda x: isinstance(x, str), lst))
print(lst)
