class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = ""
        maxHeap = []
        for count, char in [(-a, "a"), (-b, "b"), (-c, "c")]:
            if count != 0:
                heapq.heappush(maxHeap, (count, char))

        while maxHeap:
            count, char = heapq.heappop(maxHeap)
            if len(res)>1 and res[-1]==res[-2]==char:
                if not maxHeap:
                    break
                count1,char1 = heapq.heappop(maxHeap)
                res=res+char1
                if count1+1!=0:
                    heapq.heappush(maxHeap, (count1+1,char1))
                heapq.heappush(maxHeap,(count,char))
            else:
                res = res+char
                if count+1!=0:
                    heapq.heappush(maxHeap,(count+1,char))
        return res

    