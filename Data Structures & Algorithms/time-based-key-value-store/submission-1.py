class TimeMap:

    def __init__(self):
        self.timestamps = defaultdict(dict)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # if key not in self.timestamps:
        #     self.timestamps[key]={}
        self.timestamps[key][timestamp]=value                

    def get(self, key: str, timestamp: int) -> str:
        act=0
        if key not in self.timestamps:
            return ""
        for ts in self.timestamps[key].keys():
            if ts<=timestamp:
                act = max(act,ts)
        return "" if act==0 else self.timestamps[key][act]

        
