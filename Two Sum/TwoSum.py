def twoSum(self, nums: List[int], target: int) -> List[int]:
    for i in range(0, len(nums)):
        try:
            n = target - nums[i]
            p = nums.index(n)
            if p is not i:
                if p>i:
                    return [i,p]
                else:
                    return [p,i]
        except:
            continue