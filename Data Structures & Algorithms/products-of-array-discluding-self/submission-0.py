class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        combinedProduct = 1
        zeroIdx = []

        for idx, num in enumerate(nums):
            if num == 0:
                zeroIdx.append(idx)
            else:
                combinedProduct *= num

        if len(zeroIdx) > 1:
            return [0] * len(nums)
        
        retList = []
        for idx, num in enumerate(nums):
            if len(zeroIdx) == 1:
                if zeroIdx[0] == idx:
                    retList.append(combinedProduct)
                else:
                    retList.append(0)
            else:
                retList.append(int(combinedProduct/num))
        
        return retList