class Solution:
    def reorganizeString(self, s: str) -> str:
        st=defaultdict(int)
        st = Counter(s)
        minHeap=[]
        res=""
        prev = None
        for key,value in st.items():
            heapq.heappush(minHeap,(-value,key))
        while minHeap or prev:
            if prev and not minHeap:
                return ""
            cnt,char = heapq.heappop(minHeap)
            res = res+char
            cnt+=1
            if prev:
                heapq.heappush(minHeap, prev)
                prev=None
            if cnt!=0:
                prev = (cnt,char)
            
        return res


        

        