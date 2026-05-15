class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        firstIndex = 0
        lastIndex = len(s) - 1
        while firstIndex < lastIndex and lastIndex > firstIndex:
            
            while not s[firstIndex].isalnum() and firstIndex < lastIndex:
                firstIndex += 1
            while not s[lastIndex].isalnum() and lastIndex > firstIndex:
                lastIndex -= 1

            print(firstIndex, lastIndex)
            char1 = s[firstIndex]
            char2 = s[lastIndex]
            print(char1, char2)

            if char1.lower() != char2.lower() and char1.isalnum() and char2.isalnum():
                return False

            firstIndex += 1
            lastIndex -= 1

        return True
        