class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lowIdx = 0
        highIdx = len(nums)-1

        while lowIdx <= highIdx:
            midpoint = int((highIdx - lowIdx)/2) + lowIdx
            midNum = nums[midpoint]

            if midNum == target:
                return midpoint
            elif nums[midpoint] < target:
                lowIdx = midpoint + 1
            else:
                highIdx = midpoint - 1
        
        return -1
            
