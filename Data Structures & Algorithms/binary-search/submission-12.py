class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
    
        while(left <= right):
            midpoint = (right + left) //2
            midpointVal = nums[midpoint]
            
            if (midpointVal == target):
                return midpoint
            elif target < midpointVal:
                right = midpoint - 1
            else:
                left = midpoint + 1
        
        return -1