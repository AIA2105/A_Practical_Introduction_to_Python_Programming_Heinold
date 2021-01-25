def first_diff(string1, string2):
    if string1 == string2:
        return -1
    else:
        mylen = min(len(string1), len(string2))
        for i in range(mylen):
            if string1[i] != string2[i]:
                return i
        return i + 1


print(first_diff('ahmed', 'as'))
