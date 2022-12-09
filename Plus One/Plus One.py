import collections

def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    new_digits = collections.deque()
    additional = 1
    for i in range(len(digits)-1, -1, -1):
        sum1 = digits[i]+additional
        if sum1>9:
            new_digits.appendleft(0)
            additional = 1
        else:
            new_digits.appendleft(sum1)
            additional = 0

    if additional>0:
        new_digits.appendleft(additional)

    return new_digits

print(plusOne([1,2,3]))