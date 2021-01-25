def number_of_factors(num):
    sum = 0
    for i in range(1, num + 1):
        if num % i == 0:
            sum = sum + 1
    return sum


print(number_of_factors(4))
