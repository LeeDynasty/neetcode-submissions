class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        complementDict = {}

        for idx, num in enumerate(numbers):
            complementDict[num] = idx+1
        
        retList = []
        for idx, num in enumerate(numbers):
            if (target - num) in complementDict:
                retList.append(idx+1)
                retList.append(complementDict[target-num])
                return retList
        return retList