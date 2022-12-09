
def lengthOfLastWord(self, s):
    """
    :type s: str
    :rtype: int
    """
    counter = 0
    last_length = 0
    for x in s:
        if x != " ":
            counter += 1
        else:
            if counter>0:
                last_length = counter

            counter = 0

    if counter>0:
        last_length = counter 

    return (last_length)