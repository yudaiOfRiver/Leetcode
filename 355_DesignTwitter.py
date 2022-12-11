class Twitter:
    def __init__(self):
        self.userIds = []
        self.tweetIds = []
        self.relations = [[0] for _ in range(500)]

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetIds.append([userId, tweetId])

    def getNewsFeed(self, userId: int) -> list[int]:
        feeds = []
        for uid, tid in self.tweetIds[::-1]:
            if uid in self.relations[userId] or uid == userId:
                feeds.append(tid)
            if len(feeds) == 10:
                break
        return feeds

    def follow(self, followerId: int, followeeId: int) -> None:
        self.relations[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.relations[followerId].remove(followeeId)

obj = Twitter()
print(obj.postTweet(1, 5))
print(obj.getNewsFeed(1))
print(obj.follow(1, 2))
print(obj.postTweet(2, 6))
print(obj.getNewsFeed(1))
print(obj.unfollow(1, 2))
print(obj.getNewsFeed(1))



