# import requests
# from requests.auth import HTTPBasicAuth
# 
# auth = HTTPBasicAuth('m5Q5N6H9lFZ-qw', '71pM2Gcqcr0QdbycdusmATGs7TI')
# post_data = {
#     "grant_type": "authorization_code",
#     "redirect_uri": "http://www.github.com/jsfuentes",
#     "code": "IcXWREloCuL3RcL1XIXB8nh9aXE"
# }
# headers = {"User-Agent": "android:mysignal:v0.1 (by /u/yourcousinbob)"}
# x = requests.get('https://www.reddit.com/api/v1/access_token', auth=auth, data=post_data, headers=headers)
# print(x.json())

import praw

#Step One 
def getCode():
    reddit = praw.Reddit(client_id='m5Q5N6H9lFZ-qw',
                         client_secret='71pM2Gcqcr0QdbycdusmATGs7TI',
                         redirect_uri='http://127.0.0.1:5000/',
                         user_agent='android:mysignal:v0.1 (by /u/yourcousinbob)')
    print(reddit.auth.url(['identity'], '...', 'permanent'))

def authCode():
    reddit = praw.Reddit(client_id='m5Q5N6H9lFZ-qw',
                         client_secret='71pM2Gcqcr0QdbycdusmATGs7TI',
                         redirect_uri='http://127.0.0.1:5000/',
                         user_agent='android:mysignal:v0.1 (by /u/yourcousinbob)')
    refresh_token = reddit.auth.authorize("_Mo4kGqGRhs9N5xa6g9KNMGCGyI")
    print(refresh_token)
    print(reddit.user.me())
    
# authCode()
    
