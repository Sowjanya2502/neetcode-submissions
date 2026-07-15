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
            if prev and len(minHeap)==0:
                return ""
            freq,letter = heapq.heappop(minHeap)
            if prev:
                heapq.heappush(minHeap, prev)
                prev = None
            if freq+1!=0:
                prev = (freq+1,letter)
            res =res+letter
        return res
            



        

        