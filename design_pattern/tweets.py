class Twitter(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        # key is user id, value is followers
        self.users = {}
        """
          users = {
             "user_one": [follower1, follwer2]
          }
        """
        # key is user id, value is tweet id and time also content
        """
        tweets = {
          "user_1": [{
           (tweet_1, time),
           (tweet_2, time)
          }],
          "user_2":[
           (time, tweet),
           (time, tweet)
          ]
        }
        """
        self.tweets = {}
        self.time = 0

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        #import datetime
        tweet = (self.time, str(tweetId))
        if userId in self.tweets:
            self.tweets[userId].append(tweet)
        else:
            self.tweets[userId] = [tweet]
        self.time += 1

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        import heapq
        feeds = []
        user_followees = [userId]
        for user_id, followers in self.users.iteritems():
            if userId in followers:
                user_followees.append(user_id)
        print userId,  " followed ", user_followees
        for user_id, tweets in self.tweets.iteritems():
            temp_sorted_tweets = []
            if user_id in user_followees:
                for tweet in tweets:
                    heapq.heappush(temp_sorted_tweets, tweet)
                num_temp = len(temp_sorted_tweets)
                num = 10
                if num_temp < 10:
                    num = num_temp
                for i in range(num, 0, -1):
                    heapq.heappush(feeds, temp_sorted_tweets[-1*i])
        print "feeds:", feeds

        def getKey(item):
            return item[0]

        feeds = sorted(feeds, key=getKey)
        print 'new feeds:', feeds
        num_feeds = len(feeds)
        num = 10
        if num > num_feeds:
            num = num_feeds
        result = []
        for i in range(num, 0, -1):
            time, tweet_id = feeds[-1*(num+1-i)]
            print time, ' - ', tweet_id
            result.append(int(tweet_id))
            print 'result:', result
        return result

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followeeId not in self.users:
            self.users[followeeId] = []
        self.users[followeeId].append(followerId)

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        try:
            follower_index = self.users[followeeId].index(followerId)
            del self.users[followeeId][follower_index]
        except:
            pass


# Your Twitter object will be instantiated and called as such:
obj = Twitter()

obj.postTweet(2, 5)
obj.postTweet(1, 3)
obj.postTweet(1, 101)
obj.postTweet(2, 13)
obj.postTweet(2, 10)
obj.postTweet(1, 2)
obj.postTweet(2, 94)
obj.postTweet(2, 505)
obj.postTweet(1, 333)
obj.postTweet(1, 22)
for tweet in obj.tweets:
    print tweet

param_2 = obj.getNewsFeed(2)
print param_2

obj.follow(2, 1)

param_2 = obj.getNewsFeed(2)
print param_2