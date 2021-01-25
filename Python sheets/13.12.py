def findall(string, char):
    loc = []
    for i in range(len(string)):
        if string[i] == char:
            loc.append(i)
    return loc


print(findall('allah akbar', 'z'))
