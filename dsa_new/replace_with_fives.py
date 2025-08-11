# def replaceWithFives(n):
#     return int(str(n).replace('0', '5'))

# n = int(input())
# print(replaceWithFives(n))

def replace_zeros_with_five(number):
    result = 0
    multiplier = 1

    if number == 0:
        return 5

    while number > 0:
        digit = number % 10
        if digit == 0:
            digit = 5
        result += digit * multiplier
        multiplier *= 10
        number //= 10

    return result


N = int(input())
print(replace_zeros_with_five(N))
