class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramDict = {}

        for curStr in strs:
            curStrArr = [0] * 26
            
            for curLetter in curStr:
                curStrArr[ord(curLetter.lower())-97] += 1

            curStrTuple = tuple(curStrArr)
            if curStrTuple in anagramDict:
                anagramDict[curStrTuple].append(curStr)
            else:
                anagramDict[curStrTuple] = [curStr]
        returnArr = []

        for key, value in anagramDict.items():
            returnArr.append(value)
        return returnArr

            