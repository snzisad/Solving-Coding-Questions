
def climbStairs(self, n):
    """
    :type n: int
    :rtype: int
    """
    cur = 1
    pre = 1
    temp = 0
    
    for i in range(1, n):
        temp = cur
        cur += pre
        pre = temp
        
    return cur