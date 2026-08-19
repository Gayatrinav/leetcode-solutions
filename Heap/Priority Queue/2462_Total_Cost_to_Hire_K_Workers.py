import heapq

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)

        left_heap = []
        right_heap = []

        left = 0
        right = n - 1
        total = 0

        for _ in range(k):

            while len(left_heap) < candidates and left <= right:
                heapq.heappush(left_heap, costs[left])
                left += 1

            while len(right_heap) < candidates and left <= right:
                heapq.heappush(right_heap, costs[right])
                right -= 1

            if not left_heap:
                total += heapq.heappop(right_heap)

            elif not right_heap:
                total += heapq.heappop(left_heap)

            elif left_heap[0] <= right_heap[0]:
                total += heapq.heappop(left_heap)

            else:
                total += heapq.heappop(right_heap)

        return total