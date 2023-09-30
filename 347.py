class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        for num in nums:
            d[num] += 1

        counts = defaultdict(list)
        for num in d:
            count = d[num]
            counts[count].append(num)

        result = []
        top = sorted(counts.keys(), reverse=True)
        i = 0
        while (k > 0 and i < len(top)):
            nums = counts[top[i]]
            for num in nums:
                if k == 0:
                    return result
                result.append(num)
                k -= 1
            i += 1
        return result
        