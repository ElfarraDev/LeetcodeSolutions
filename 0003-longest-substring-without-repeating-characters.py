class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = longest = 0

        for right in range(len(s)):

            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            longest = max(longest,right - left + 1)
            seen.add(s[right])

        return longest
