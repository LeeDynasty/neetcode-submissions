class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        bestResult = 0

        count = {}
        left = 0
        maxLen = 0

        for right in range(len(s)):
            # Get number of repeating char in current window
            count[s[right]] = count.get(s[right], 0) + 1

            # Update best repeating char with expanded window
            maxLen = max(maxLen, count[s[right]])

            while(right - left + 1) - maxLen > k:
                count[s[left]] -= 1
                left += 1

            bestResult = max(right - left + 1, bestResult)
        
        return bestResult