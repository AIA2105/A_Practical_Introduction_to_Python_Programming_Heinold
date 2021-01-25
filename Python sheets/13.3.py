def sum_digits(num):
    string = str(num)
    sum1 = 0
    for i in range(len(string)):
        sum1 = sum1 + int(string[i])
    return sum1


print(sum_digits(1234))
