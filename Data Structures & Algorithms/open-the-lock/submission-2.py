class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if '0000' in deadends:
            return -1
        visited=set(deadends)
        que = deque()
        que.append(['0000',0])
        def children(lock):
            res=[]
            for i in range(4):
                digit = str((int(lock[i])+1)% 10)
                digit1 = str(((int(lock[i])-1)+10) % 10)
                res.append(lock[:i]+digit+lock[i+1:])
                res.append(lock[:i]+digit1+lock[i+1:])
            return res
            
        while que:
            lock,turn = que.popleft()
            if lock == target:
                return turn
            for child in children(lock):
                if child not in visited:
                    visited.add(child)
                    que.append([child,turn+1])
        return -1