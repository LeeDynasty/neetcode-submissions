class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        searchList = set()
        for curNum in nums:
            if curNum in searchList:
                return True
            else:
                searchList.add(curNum)

        return False