import collections

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numDict = Counter(nums)
        freqAry = [0] * (len(nums)+1)

        for num, count in numDict.items():
            if freqAry[count] == 0:
                freqAry[count] = [num]
            else:
                freqAry[count].append(num)

        retList = []
        for frequency, numList in enumerate(freqAry):
            if numList == 0:
                continue
            else:
                retList.extend(numList)
    
        return retList[len(retList)-k:]