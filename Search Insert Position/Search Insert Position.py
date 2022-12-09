
def searchInsert(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """

    if nums[0]>=target:
        return 0

    if nums[-1]<target:
        return len(nums)

    start = 0
    end = len(nums)

    while 1:
        mid_pos = int((start+end)/2)
        if nums[mid_pos-1]<target<=nums[mid_pos]:
            return mid_pos

        elif nums[mid_pos]<target:
            start = mid_pos+1
            
        else:
            end = mid_pos-1