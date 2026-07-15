class ListNode:
    def __init__(self,key,value):
        self.key,self.value =key,value
        self.prev,self.next = None, None

class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.mpkv = dict()
        self.mpfl = defaultdict(OrderedDict)
        self.minfreq = 0

    def get(self, key: int) -> int:
        if key not in self.mpkv:
            return -1
        freq,val = self.mpkv[key]
        del self.mpfl[freq][key]
        if self.minfreq == freq and not self.mpfl[freq]:
            self.minfreq+=1
        self.mpkv[key]=(freq+1, val)
        self.mpfl[freq+1][key]=val
        return self.mpfl[freq+1][key]

    def put(self, key: int, value: int) -> None:
        if key in self.mpkv:
            self.get(key)
            self.mpkv[key]=(self.mpkv[key][0],value)
            self.mpfl[self.mpkv[key][0]][key]=value
        if self.cap == len(self.mpkv):
            k, v = self.mpfl[self.minfreq].popitem(last=False)
            del self.mpkv[k]
        self.mpkv[key]=(1,value)
        self.mpfl[1][key]=value
        self.minfreq = 1


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
