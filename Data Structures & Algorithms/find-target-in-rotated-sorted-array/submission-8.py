class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # First, find the minimum index to see the rotation amount

        left, right = 0, len(nums)-1

        while (left < right):
            midpoint = left + ((right - left) // 2)

            if (nums[midpoint] < nums[right]):
                right = midpoint 
            else:
                left = midpoint + 1

        # Minimum is at left. If target is less than right item in array, search from left to right. Otherwise, Search from first to minimum.
        minVal = nums[left]
        minIdx = left

        # We can just calculate the appropriate start/stop index- no need to split arrays
        left, right = minIdx, len(nums)-1
        if target > nums[len(nums)-1]:
            left, right = 0, minIdx-1
        
        while (left <= right):
            midpoint = left + ((right - left) // 2)
            
            if nums[midpoint] == target:
                return midpoint 
            elif (target > nums[midpoint]):
                left = midpoint + 1
            else:
                right = midpoint - 1

        return -1