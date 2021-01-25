def matches(str1, str2):
    mylen=0
    sum = 0
    if len(str1) <= len(str2):
        mylen = len(str1)
    else:
        mylen = len(str2)
    for i in range(mylen):
        if str1[i] == str2[i]:
            sum = sum + 1
    return sum


print(matches('python', 'path'))
