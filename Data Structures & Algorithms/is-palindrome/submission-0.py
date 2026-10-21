class Solution:
    def isPalindrome(self, s: str) -> bool:
        strippedStr = "".join([char for char in s.lower() if (char.isalnum())])
        reverseStr = strippedStr[::-1]
        if reverseStr == strippedStr:
            return True

        return False