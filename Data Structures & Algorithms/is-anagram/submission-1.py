class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sList = {}
        for sLetter in s:
            if sLetter in sList:
                sList[sLetter] = sList[sLetter] + 1
            else:
                sList[sLetter] = 1
        
        for tLetter in t:
            if tLetter not in sList:
                return False
            elif sList[tLetter] == 0:
                return False
            else:
                sList[tLetter] = sList[tLetter] - 1

        
        return True