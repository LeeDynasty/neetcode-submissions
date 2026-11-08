class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        startPtr = 0
        endPtr = len(numbers) - 1
        found = False

        while not found:
            currSum = numbers[startPtr] + numbers[endPtr]
            if currSum == target:
                return [startPtr+1, endPtr+1]
            elif currSum > target:
                endPtr -= 1
            else:
                startPtr += 1
        


        # complementDict = {}

        # for idx, num in enumerate(numbers):
        #     complementDict[num] = idx+1
        
        # retList = []
        # for idx, num in enumerate(numbers):
        #     if (target - num) in complementDict:
        #         retList.append(idx+1)
        #         retList.append(complementDict[target-num])
        #         return retList
        # return retList