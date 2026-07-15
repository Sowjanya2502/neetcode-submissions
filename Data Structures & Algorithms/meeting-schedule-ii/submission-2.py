"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals)==0:
            return 0
        points = []
        overlap,max_result = 0,0
        for inv in intervals:
            points.append((inv.start,'S'))
            points.append((inv.end,'E'))
        points.sort(key=lambda x: (x[0],x[1]))
        for inv,points in points:
            if points == 'S':
                overlap+=1
            else:
                overlap-=1
            max_result = max(max_result,overlap)
        return max_result

        