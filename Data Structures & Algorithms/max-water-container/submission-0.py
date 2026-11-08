class Solution:
    def maxArea(self, heights: List[int]) -> int:
        startPtr = 0
        endPtr = len(heights) - 1

        maxWater = 0

        for idx in range(0, len(heights)):
            maxWater = max(maxWater, (endPtr - startPtr) * (min(heights[startPtr], heights[endPtr])))
            if (heights[startPtr] < heights[endPtr]):
                startPtr += 1
            else:
                endPtr -= 1
        return maxWater