def decimal_to_binary(decimal):
    binary = ''
    while decimal > 1:
        binary = f'{decimal % 2}' + binary
        decimal //= 2
    binary = f'{decimal}' + binary
    return binary


print(decimal_to_binary(25))


def binary_to_decimal(binary):
    decimal = ''
    for i in range(len(binary)):
        decimal += int(binary[i]) * 2 ** (len(binary) - i - 1)
    return decimal


print(binary_to_decimal(10011))
