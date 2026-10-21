class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complementArray = {}

        for numIdx, num in enumerate(nums):
            diff = target - num
            if diff in complementArray:
                return [complementArray[diff], numIdx]
            complementArray[num] = numIdx
