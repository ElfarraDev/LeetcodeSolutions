class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        r = {'I': 1, 'V': 5, 'X': 10, 'L': 50,'C': 100, 'D': 500, 'M': 1000}
        for i,n in zip(s,s[1:]):
            if r[i] < r[n]:
                res -= r[i]
            else:
                res += r[i]
        return res + r [s[-1]]
