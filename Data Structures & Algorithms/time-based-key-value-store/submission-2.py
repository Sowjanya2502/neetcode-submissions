class TimeMap:

    def __init__(self):
        self.timemap = defaultdict(dict)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemap[key][timestamp]=value
        

    def get(self, key: str, timestamp: int) -> str:
        res = 0
        if key not in self.timemap:
            return ""
        for ts in self.timemap[key].keys():
            if ts<=timestamp:
                res = max(res,ts)
        return "" if res == 0 else self.timemap[key][res]

        
