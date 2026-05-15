class Solution:
    def isValid(self, s: str) -> bool:
        # maybe one stack, for forward, then pull from the 
        # stack to compare

        openingCharacters = []
        matchingCharacters = {'}':'{', ']': '[', ')': '('}

        for char in s:
            if char in ['{', '[', '(']:
                openingCharacters.append(char)
            else:
                if len(openingCharacters) == 0 or matchingCharacters[char] != openingCharacters.pop():
                    return False
        if openingCharacters:
            return False
        else:
            return True


