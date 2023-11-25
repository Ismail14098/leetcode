class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        list = [x * -1 for x in stones]
        heapq.heapify(list)
        while len(list) > 1:
            a, b = heapq.heappop(list), heapq.heappop(list)
            if a != b:
                heapq.heappush(list, abs(a-b) * -1)
        return list[0] * -1