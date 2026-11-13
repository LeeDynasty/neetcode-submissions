class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleetStack = []
        speedDict = {}
        for idx, pos in enumerate(position):
            speedDict[pos] = speed[idx]

        position.sort(reverse = True)
        for carIdx in range(0, len(position)):
            curCarPos = position[carIdx]
            curCarSpeed = speedDict[curCarPos]
            curCarETA = (target - curCarPos) / curCarSpeed
            if fleetStack:
                stackTopETA = fleetStack[-1]
                if stackTopETA < curCarETA:
                    fleetStack.append(curCarETA)
            else:
                fleetStack.append(curCarETA)
        return int(len(fleetStack))

                