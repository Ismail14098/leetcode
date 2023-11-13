class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        def calculateHours(piles: List[int], speed: int) -> int:
            result = 0
            for pile in piles:
                result += math.ceil(pile/speed)
            return result
        
        result = r
        while l <= r:
            m = int((l + r)/2)
            curr = calculateHours(piles, m)
            if curr > h:
                l = m+1
            elif curr <= h:
                result = m
                r = m-1
        return result