import heapq

class SmallestInfiniteSet:

    def __init__(self):
        self.heap = []
        self.added = set()
        self.next_num = 1

    def popSmallest(self) -> int:
        if self.heap:
            num = heapq.heappop(self.heap)
            self.added.remove(num)
            return num

        num = self.next_num
        self.next_num += 1
        return num

    def addBack(self, num: int) -> None:
        if num < self.next_num and num not in self.added:
            heapq.heappush(self.heap, num)
            self.added.add(num)