class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        lastend = intervals[0][1]
        res = 0
        for inv in intervals[1:]:
            if lastend>inv[0]:
                res+=1
                lastend = min(lastend, inv[1])
            else:
                lastend = inv[1]
        return res
        



        