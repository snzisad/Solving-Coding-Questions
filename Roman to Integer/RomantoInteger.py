def romanToInt(s: str) -> int:
    r = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    m = [1, 5, 10, 50, 100, 500, 1000]

    y = 0
    i = 0

    while i<len(s):
        x = s[i]
        pos = r.index(s[i])

        if(i == len(s)-1):
            y = y+m[pos] 
            break

        else:
            pos2 = r.index(s[i+1])

            if (pos == 0 and (pos2 == 1 or pos2 == 2)) or (pos == 2 and (pos2 == 3 or pos2 == 4)) or(pos == 4 and (pos2 == 5 or pos2 == 6)):
                y = y + (m[pos2] - m[pos]) 
                i = i+2

            else:
                y = y+m[pos] 
                i = i+1


    return y 

print(romanToInt("LVIII"))