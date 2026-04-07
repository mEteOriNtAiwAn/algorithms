class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        start = 1
        end = max(piles)
        min_piles = float('inf')

        while start <= end:
            center = start + (end - start) // 2

            hours = sum([math.ceil(pail/ center) for pail in piles])

            if hours <= h:
                min_piles = center
                end = center - 1
            else:
                start = center + 1

        return min_piles