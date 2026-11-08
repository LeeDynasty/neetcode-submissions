class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numDict = {}

        for idx,num in enumerate(nums):
            numDict[num] = idx
        
        maxLength = 0

        for key in numDict:
            curLength = 0

            if (key-1) in numDict:
                continue
            else:
                endReached = False
                curNum = key
                while not endReached:
                    if curNum in numDict:
                        curLength += 1
                        curNum += 1
                    else:
                        endReached = True
                if maxLength < curLength:
                    maxLength = curLength
        
        return maxLength



