class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r, maxf, result = 0, 0, 0, 0
        d = defaultdict(int)
        while r < len(s):
            d[s[r]] += 1
            maxf = max(maxf, d[s[r]])
            if r-l+1-maxf>k:
                d[s[l]] -= 1
                l += 1
            result = max(result, r-l+1)
            r += 1
        return result