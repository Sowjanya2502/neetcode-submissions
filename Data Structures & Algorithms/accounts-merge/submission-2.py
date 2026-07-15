class UnionFind:
    def __init__(self, n):
        self.parent =[i for i in range(n)]
        self.size = [1]*n
    def union(self, x1, x2) -> None:
        p1,p2 = self.find(x1), self.find(x2)
        if p1!=p2:
            if self.size[p1]>self.size[p2]:
                self.parent[p2]=p1
                self.size[p1]+=self.size[p2]
            else:
                self.parent[p1]=p2
                self.size[p2]+=self.size[p1]
    def find(self, x):
        if self.parent[x]==x:
            return x
        self.parent[x]=self.find(self.parent[x])
        return self.parent[x]

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        ini = UnionFind(len(accounts))
        emailacc = {}
        for i,a in enumerate(accounts):
            for e in a[1:]:
                if e in emailacc:
                    ini.union(i, emailacc[e])
                else:
                    emailacc[e]=i
        emailgrp = defaultdict(list)
        for e,i in emailacc.items():
            par = ini.find(i)
            emailgrp[par].append(e)
        res = []
        for i,emails in emailgrp.items():
            name = accounts[i][0]
            res.append([name]+sorted(emails))
        return res
