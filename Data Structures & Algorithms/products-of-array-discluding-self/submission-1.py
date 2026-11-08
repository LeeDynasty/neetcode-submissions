class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        combinedProduct = 1
        zeroIdx = -1
        zeroCount = 0

        for idx, num in enumerate(nums):
            if num == 0:
                zeroCount+=1
                zeroIdx = idx
                if zeroCount > 1:
                    return [0] * len(nums)
            else:
                combinedProduct *= num
        
        retList = []
        for idx, num in enumerate(nums):
            if zeroIdx != -1:
                if zeroIdx == idx:
                    retList.append(combinedProduct)
                else:
                    retList.append(0)
            else:
                retList.append(int(combinedProduct/num))
        
        return retList