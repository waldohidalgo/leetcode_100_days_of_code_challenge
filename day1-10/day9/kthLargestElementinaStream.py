import heapq

class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        
        while len(self.heap) > k:
            heapq.heappop(self.heap)
        
    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        
        return self.heap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

sol=KthLargest(3,[4,5,8,2])
print(sol.add(3))
print(sol.add(5))
print(sol.add(10))
print(sol.add(9))
print(sol.add(4))