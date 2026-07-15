class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        rooms = [0]*n
        meetingcount = [0]*n

        for s,e in meetings:
            found = False
            minroom =0
            for i in range(n):
                if rooms[i]<=s:
                    rooms[i]=e
                    meetingcount[i]+=1
                    found = True
                    break
                if rooms[minroom]>rooms[i]:
                    minroom = i
                
            if found:
                continue
            meetingcount[minroom]+=1
            rooms[minroom]+=e-s
        return meetingcount.index(max(meetingcount))
            
