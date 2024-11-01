class Solution:
    def makeFancyString(self, s: str) -> str:
        count = 1
        result = [s[0]]

        for i in range(1,len(s)):
            if s[i-1] != s[i]:
                count = 1
                result.append(s[i])
            elif count < 2:
                count += 1
                result.append(s[i])
        return ''.join(result)
