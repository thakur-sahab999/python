def exponent(base, exponent):
    result = 1

    for i in range(exponent):
        result *= base
    return result

base = int(input('Enter the number: '))
ex = int(input('Enter the power: '))
print(exponent(base, ex))