class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans=[]
        hash_map=defaultdict(int)
        for i in range(len(nums)):
            hash_map[nums[i]] += 1
        heap = []
        for num, freq in hash_map.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)   # removes smallest freq

        # Step 3: Extract result
        while heap:
            ans.append(heapq.heappop(heap)[1])

        return ans
        
            