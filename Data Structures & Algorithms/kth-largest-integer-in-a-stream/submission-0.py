class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.numList = nums
        
    def add(self, val: int) -> int:
        self.numList.append(val)
        self.numList.sort()
        return self.numList[len(self.numList)-self.k]
