class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # [index, temp]
        for tempIdx, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                stackTopIdx, stackTopTemp = stack.pop()
                res[stackTopIdx] = tempIdx - stackTopIdx
            stack.append([tempIdx, temp])

        return res