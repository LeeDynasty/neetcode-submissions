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

        for i in range(len(freqAry)-1, -1, -1):
            if freqAry[i] == 0:
                continue
            else:
                retList.extend(freqAry[i])

            if len(retList) > k:
                break
    
        return retList[:k]