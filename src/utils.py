import praw

def configureReddit(config):
    reddit = praw.Reddit(client_id=config['REDDIT_ID'],
                         client_secret=config['REDDIT_SECRET'],
                         redirect_uri=config['REDDIT_REDIRECT_URI'],
                         user_agent=config['REDDIT_USER_AGENT'])
    return reddit


def getRedditOauthURL(config):
    reddit = configureReddit(config)
    return reddit.auth.url(['identity'], '...', 'permanent')

def authCode():
    reddit = praw.Reddit(client_id='m5Q5N6H9lFZ-qw',
                         client_secret='71pM2Gcqcr0QdbycdusmATGs7TI',
                         redirect_uri='http://127.0.0.1:5000/',
                         user_agent='android:mysignal:v0.1 (by /u/yourcousinbob)')
    refresh_token = reddit.auth.authorize("_Mo4kGqGRhs9N5xa6g9KNMGCGyI")
    print(refresh_token)
    print(reddit.user.me())

