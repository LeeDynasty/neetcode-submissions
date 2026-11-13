class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) -1

        while (left < right):
            midpointIdx = left + ((right - left) // 2)
            if nums[midpointIdx] < nums[right]:
                right = midpointIdx
            else:
                left = midpointIdx + 1

        return nums[left]