class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        startPtr = 0
        endPtr = len(numbers) - 1

        while startPtr < endPtr:
            currSum = numbers[startPtr] + numbers[endPtr]
            if currSum == target:
                return [startPtr+1, endPtr+1]
            elif currSum > target:
                endPtr -= 1
            else:
                startPtr += 1
        
        return []