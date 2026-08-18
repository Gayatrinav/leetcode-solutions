import heapq

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs = sorted(zip(nums1, nums2), key=lambda x: x[1], reverse=True)

        heap = []
        total = 0
        ans = 0

        for a, b in pairs:
            heapq.heappush(heap, a)
            total += a

            if len(heap) > k:
                total -= heapq.heappop(heap)

            if len(heap) == k:
                ans = max(ans, total * b)

        return ans