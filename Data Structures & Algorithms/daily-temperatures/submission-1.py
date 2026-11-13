class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # [idx, temp]
        res = [0] * len(temperatures)

        for curIdx, curTemp in enumerate(temperatures):
            while stack and curTemp > stack[-1][1]:
                stackIdx, stackTemp = stack.pop()
                res[stackIdx] = curIdx - stackIdx
            
            stack.append([curIdx, curTemp])
        return res