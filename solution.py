# Problem: Median of Stream of Integers Running Integers
# Difficulty: Hard
# Link: https://www.geeksforgeeks.org/median-of-stream-of-integers-running-integers/

class Solution:
    def __init__(self):
        self.max_heap = []  # for smaller half
        self.min_heap = []  # for larger half
    
    def addNum(self, num: int) -> None:
        if not self.max_heap or num <= -self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)
        
        # Balance the heaps
        if len(self.max_heap) > len(self.min_heap) + 1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        elif len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
    
    def findMedian(self) -> float:
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        else:
            return -self.max_heap[0]

########################################
# if __name__ == '__main__':
#     s = Solution()
#     # print(s.solve(inputs...))