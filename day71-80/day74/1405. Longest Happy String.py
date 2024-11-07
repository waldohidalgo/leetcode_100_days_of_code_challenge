import heapq
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        if a > 0:
            heapq.heappush(heap, (-a, 'a'))
        if b > 0:
            heapq.heappush(heap, (-b, 'b'))
        if c > 0:
            heapq.heappush(heap, (-c, 'c'))

        result = ""

        while heap:
            freq1, char1 = heapq.heappop(heap)
            if len(result) >= 2 and result[-1] == result[-2] == char1:
                if not heap:
                    break
                freq2, char2 = heapq.heappop(heap)
                result+=char2
                freq2 += 1
                if freq2 < 0:
                    heapq.heappush(heap, (freq2, char2))
                heapq.heappush(heap, (freq1, char1)) 
            else:
                result+=char1
                freq1 += 1
                if freq1 < 0:
                    heapq.heappush(heap, (freq1, char1))
        
        return result
                

sol=Solution()
word=sol.longestDiverseString(0,8,11)
print(word)
