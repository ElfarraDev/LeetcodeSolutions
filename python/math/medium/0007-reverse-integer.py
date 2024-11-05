class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x >= 0 else -1
        x = abs(x)
        reverse = 0

        while x:
            reverse = (reverse * 10) + x % 10
            x //= 10

        if reverse > 2**31 - 1 or reverse < -2**31:
            return 0

        return sign * reverse
