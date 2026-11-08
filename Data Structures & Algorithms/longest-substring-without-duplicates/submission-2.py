class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        startPtr = 0
        endPtr = 0
        curSubstringLetters = {}
        curSubstringLetters[s[startPtr]] = startPtr

        curMaxLength = 1
        curLength = 1

        while (endPtr<len(s)-1):
            curLength += 1
            endPtr += 1
            if s[endPtr] in curSubstringLetters:
                # Move the startPtr to the originalIdx + 1, removing letters along the way
                originalIdx = curSubstringLetters[s[endPtr]]
                for i in range(originalIdx - startPtr +1):
                    curLength -= 1
                    curSubstringLetters.pop(s[startPtr + i])
                startPtr = originalIdx+1
                curSubstringLetters[s[endPtr]] = endPtr
                continue
            curMaxLength = max(curMaxLength, curLength)
            curSubstringLetters[s[endPtr]] = endPtr
            
        return curMaxLength