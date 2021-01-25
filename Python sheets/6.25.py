exp = input("Enter the expression:")
newExp = ""

for i in range(len(exp)-1):
    if exp[i].isalnum() and (exp[i+1].isalpha() or exp[i+1] == '('):
        newExp=newExp+exp[i]+'*'
    else:
        newExp = newExp + exp[i]

print(newExp+exp[-1])