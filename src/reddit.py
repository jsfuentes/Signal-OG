import praw
from .models import redditToPost

class Reddit:
    def __init__(self, config, refresh_token=None):
        self.config = config
        self._setReddit(refresh_token)
        
    def _setReddit(self, refresh_token=None):
        reddit_config = {
            'client_id': self.config['REDDIT_ID'],
            'client_secret': self.config['REDDIT_SECRET'],
            'redirect_uri': self.config['REDDIT_REDIRECT_URI'],
            'user_agent': self.config['REDDIT_USER_AGENT']
        }
        if refresh_token is not None:
            reddit_config['refresh_token'] = refresh_token
        self.reddit = praw.Reddit(**reddit_config)
    
    def getOauthURL(self):
        return self.reddit.auth.url(['identity', 'read', 'mysubreddits'], '...', 'permanent')
        
    def getRefreshToken(self, code):
        refresh_token = self.reddit.auth.authorize(code)
        print(self.reddit.user.me())
        self._setReddit(refresh_token)
        return refresh_token
    
    def getSubreddits(self):
        return list(self.reddit.user.subreddits(limit=None))
        
    def getFront(self, limit):
        front = self.reddit.front.best(limit=limit) #returns submissions
        parsed_front = []
        for post in front:
            # print(post.name)
            parsed_front.append(redditToPost(post))
        # print("reddit", parsed_front)
        return parsed_front
