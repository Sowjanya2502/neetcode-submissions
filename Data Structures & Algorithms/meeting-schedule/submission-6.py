"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals)==0 or len(intervals)==1:
            return True
        intervals.sort(key=lambda x:(x.start, x.end))
        preend = [intervals[0]]
        res=0
        for inv in intervals[1:]:
            latest = preend[-1]
            if latest.end>inv.start:
                res+=1
                if res >=1:
                    return False
            else:
                preend.append(inv)
        return True

