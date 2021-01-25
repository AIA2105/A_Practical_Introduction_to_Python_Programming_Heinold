def enc(string):
    even = odd = ""
    for i in range(0, len(string), 2):
        even = even + string[i]
        if i + 1 < len(string):
            odd = odd + string[i + 1]
    return even + odd


def dec(string):
    new = ""
    for i in range(int(len(string) / 2) + 1):
        new = new + string[i]
        n = int(len(string) / 2) + i + 1
        if n < len(string):
            new = new + string[n]

    return new


s = input('Enter the string: ')
x = enc(s)
print(x)
print(dec(x))
