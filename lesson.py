def decimal_to_binary(decimal):
    binary = ''
    while decimal > 1:
        binary = f'{decimal % 2}' + binary
        decimal //= 2
    binary = f'{decimal}' + binary
    return binary


print(decimal_to_binary(15))
