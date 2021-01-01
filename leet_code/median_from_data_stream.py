"""
Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

For example,
[2,3,4], the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.
"""


import heapq

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.loheap = [] # max heap -- holds negative version of each num
        self.hiheap = [] # min heap

    def addNum(self, num: int) -> None:
        heappush(self.loheap, 0 - num)
        heappush(self.hiheap, 0 - heappop(self.loheap))
        if len(self.loheap) < len(self.hiheap):
            heappush(self.loheap, 0 - heappop(self.hiheap))

    def findMedian(self) -> float:
        if len(self.loheap) == len(self.hiheap):
            return (self.hiheap[0] - self.loheap[0]) / 2
        return 0 - self.loheap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()