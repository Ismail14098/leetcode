class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r, result = 0, 0, 0
        tmp = set()
        while r < len(s):
            if s[r] in tmp:
                while True:
                    tmp.remove(s[l])
                    l += 1
                    if s[l-1] == s[r]:
                        break
            tmp.add(s[r])
            result = max(result, r-l+1)
            r += 1
        return result