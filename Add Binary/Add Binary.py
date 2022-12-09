
def addBinary(self, a, b):
    """
    :type a: str
    :type b: str
    :rtype: str
    """

    num_1 = int(a, 2)
    num_2 = int(b, 2)
    sum_val = num_1+num_2
    
    return format(sum_val, "b")

def addBinary2(a, b):
    """
    :type a: str
    :type b: str
    :rtype: str
    """

    sums = ""
    carry = 0
    while a != "" and b != "":
        sum1, carry = binary_sum(int(a[-1]), int(b[-1]), carry)
        sums = str(sum1)+sums
        a = a[:-1]
        b = b[:-1]

    while a != "":
        sum1, carry = binary_sum(int(a[-1]), 0, carry)
        sums = str(sum1)+sums
        a = a[:-1]

    while b != "":
        sum1, carry = binary_sum(0, int(b[-1]), carry)
        sums = str(sum1)+sums
        b = b[:-1]

    if carry == 1:
        sums = str(carry)+sums

    return (sums) 
    

def binary_sum(a, b, carry):
    sum1 = (a+b+carry)
    if sum1 <= 1:
        carry = 0
    elif sum1 == 2:
        sum1 = 0
        carry = 1
    elif sum1 == 3:
        sum1 = 1
        carry = 1

    return sum1, carry