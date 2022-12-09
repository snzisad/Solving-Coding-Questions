def isValid(s: str) -> bool:
    if len(s) == 0:
        return True
    elif len(s)%2 == 1:
        return False

    brac = ['(', '{', '[']
    brac2 =[ ')', '}', ']']

    a = []

    for i in range(len(s)):
        x = s[i]

        if x in brac:    
            a.append(brac.index(x))

        elif len(a)>0 and a[-1] == brac2.index(x):
                a = a[:-1]
        else:
            return False


    if(len(a)>0):
        return False
    else:
        return True


print(isValid("()[]{}"))