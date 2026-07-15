class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.follows = defaultdict(set)
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.count,tweetId])
        self.count +=1
        
    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []
        self.follows[userId].add(userId)
        for ids in self.follows[userId]:
            for key,value in self.tweets[ids]:
                heapq.heappush(minHeap, (key,value))
                if len(minHeap)>10:
                    heapq.heappop(minHeap)
        while minHeap:
            res.append(heapq.heappop(minHeap)[1])
        return res[::-1]


    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)
        
