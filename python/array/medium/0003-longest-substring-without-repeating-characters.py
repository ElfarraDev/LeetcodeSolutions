class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window_start = 0
        max_length = 0
        char_map = {}

        for window_end in range(len(s)):
            char = s[window_end]

            if char in char_map and char_map[char] >= window_start:
                window_start = char_map[char] + 1

            char_map[char] = window_end
            current_length = window_end - window_start + 1
            max_length = max(max_length, current_length)

        return max_length
