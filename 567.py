class Solution:
    def compare(self, d1: dict, d2: dict) -> bool:
        for k in d1:
            if d1[k] != d2[k]:
                return False
        for k in d2:
            if d1[k] != d2[k]:
                return False
        return True
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d1 = defaultdict(int)
        for s in s1:
            d1[s] += 1
        l, r = 0, 0
        d2 = defaultdict(int)
        while r < len(s2):
            d2[s2[r]] += 1
            if r-l+1 > len(s1):
                d2[s2[l]] -= 1
                l += 1
            if r-l+1 == len(s1) and self.compare(d1, d2) is True:
                return True
            r += 1
        return False