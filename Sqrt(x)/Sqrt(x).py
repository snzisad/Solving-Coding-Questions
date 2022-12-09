
def mySqrt(x):
    """
    :type x: int
    :rtype: int
    """
    left, right = 0, x
    
    while left<=right:
        mid = (right + left) // 2
        sqr = mid*mid
        
        if sqr>x:
            right = mid-1
        elif sqr<x:
            left = mid+1
        else:
            return mid
    
    return right

print(mySqrt(9))