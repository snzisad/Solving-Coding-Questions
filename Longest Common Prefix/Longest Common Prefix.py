def longestCommonPrefix(strs):
    x = ""
    
    if len(strs) <= 0:
        return x
        
    s = strs[0]

    for i in range(len(s)):
        x = x+s[i]

        for j in range(1, len(strs)):
            if strs[j].startswith(x):
                pass
            
            else:
                return x[:-1]
    
    return x

print(longestCommonPrefix(["flower","flow","flight"]))