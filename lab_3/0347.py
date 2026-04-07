import heapq

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        max_heap = []
        dict_frequ = dict()

        for num in nums:
            dict_frequ[num] = dict_frequ.get(num, 0) + 1

        for num, frequ in dict_frequ.items():
            heapq.heappush(max_heap, (-frequ, num))

        return [heapq.heappop(max_heap)[1] for i in range(k)]