class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        lookup = set(jewels)
        count = 0

        for stone in stones:
            if stone in jewels:
                count += 1

        return count
