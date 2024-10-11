class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair = {')': '(', '}':'{',']':'['}

        for char in s:
            if char in pair:
                if not stack or stack.pop() != pair[char]:
                    return False
            else:
                stack.append(char)

        return len(stack) == 0
