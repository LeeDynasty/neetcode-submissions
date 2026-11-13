class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
    
        for i in range(0, 10):
            midpoint = int((right - left) // 2) + left
            print(midpoint)
            midpointVal = nums[midpoint]
            
            if (midpointVal == target):
                return midpoint
            elif target < midpointVal:
                right = midpoint - 1
            else:
                left = midpoint + 1
        
        return -1