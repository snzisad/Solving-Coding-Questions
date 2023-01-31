import collections

def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    new_digits = collections.deque()
    carry = 1
    for i in range(len(digits)-1, -1, -1):
        sum1 = digits[i]+carry
        if sum1>9:
            new_digits.appendleft(0)
            carry = 1
        else:
            new_digits.appendleft(sum1)
            carry = 0

    if carry>0:
        new_digits.appendleft(carry)

    return new_digits

print(plusOne([1,2,3]))