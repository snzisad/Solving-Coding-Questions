def isPalindrome(x: int) -> bool:
    if x<0:
        return False
    if x == 0:
        return True
    
    s = str(x)
    
    i = 0
    j = len(s)-1
    
    while i<j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    
    return True

print(isPalindrome(121))
