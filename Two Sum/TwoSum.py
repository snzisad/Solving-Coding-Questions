def twoSum(self, nums: List[int], target: int) -> List[int]:
    for i in range(0, len(nums)):
        remaining_numbers = {}

        for i, n in enumerate(nums):
            if n in remaining_numbers:
                return [i, remaining_numbers[n]]
                
            remaining_numbers[target-n] = i