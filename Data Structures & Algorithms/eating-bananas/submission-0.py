import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # The maximum eating rate will be the max of the piles- then h would be the length of the piles array
        curSpeed = max(piles)
        
        # To get the number of hours to eat at a certain rate, one pile is ceil(numInPile/eatingRate)

        bottom = 1
        top = curSpeed

        while(bottom <= top):
            midpointRate = bottom + ((top - bottom) // 2)
            # Get number of hours to finish at midpoint eating speed
            midpointHours = 0
            for bananas in piles:
                midpointHours += math.ceil( bananas / midpointRate)
            
            if midpointHours > h:
                # If midpoint hours is too high, we need to increase the eating speed
                bottom = midpointRate + 1
            else:
                # If the hours is lower than target, we can increase the eating speed
                top = midpointRate - 1
                curSpeed = midpointRate
        return curSpeed

