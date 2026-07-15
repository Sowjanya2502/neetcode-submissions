class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        index = []
        res = [0]*len(temperatures)
        for i,t in enumerate(temperatures):
            while index and index[-1][0]<t:
                sti, stt = index.pop()
                res[stt] = i-stt
            index.append((t,i))
        return res


