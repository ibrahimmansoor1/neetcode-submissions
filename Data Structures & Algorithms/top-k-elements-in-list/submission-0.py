class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:

        #count dictionary, adding num w their frequencies to count
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        #heap, adding to the heap and popping if len(heap) is more than k
        heap = []
        for num in count.keys():
            heapq.heappush(heap, (count[num],num))
            if len(heap) > k:
                heapq.heappop(heap)       
    

        #result, iterate through the end of the heap and heap[1]

        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
        

