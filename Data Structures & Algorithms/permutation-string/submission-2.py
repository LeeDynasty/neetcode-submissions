class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        counts1 = [0] * 26
        counts2 = [0] * 26
        for i in range(len(s1)):
            counts1[ord(s1[i]) - ord('a')] += 1
            counts2[ord(s2[i]) - ord('a')] += 1
        
        numMatches = 0
        for i in range(26):
            if counts1[i] == counts2[i]:
                numMatches += 1

        left = 0
        for right in range(len(s1), len(s2)):
            if numMatches == 26:
                return True
            
            # Update left side
            
            leftOrd = ord(s2[left]) - ord('a')
            counts2[leftOrd] -= 1
            if counts1[leftOrd] == counts2[leftOrd]:
                numMatches += 1
            elif counts1[leftOrd]-1 == counts2[leftOrd]:
                numMatches -= 1

            # Update right side
            rightOrd = ord(s2[right]) - ord('a')
            counts2[rightOrd] += 1
            if counts1[rightOrd] == counts2[rightOrd]:
                numMatches += 1
            elif counts1[rightOrd] +1 == counts2[rightOrd]:
                numMatches -= 1

            left += 1

        return numMatches == 26