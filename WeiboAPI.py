# -*- coding: utf-8 -*-

'''
python interpreter version: 2.7
Use the public weibo API to access data.
All you have to do is register an account of developer,
which can be done from this website page http://open.weibo.com/.
Then you will get a set consisting of app key and app secret.
'''


from weibo import APIClient
import webbrowser  # python内置的包

# App Key：1446189913
# App Secret：b7064caa3cc2153889a864d8fc8aa7ff

APP_KEY = '1446189913'  # 注意替换这里为自己申请的App信息
APP_SECRET = 'b7064caa3cc2153889a864d8fc8aa7ff'
CALLBACK_URL = 'http://api.weibo.com/oauth2/default.html'  # 回调授权页面

# 利用官方微博SDK
client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
# 得到授权页面的url，利用webbrowser打开这个url
url = client.get_authorize_url()
print (url)
webbrowser.open_new(url)

# 获取code=后面的内容
print '输入url中code后面的内容后按回车键：'
code = raw_input()
# code = your.web.framework.request.get('code')
# client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
r = client.request_access_token(code)
access_token = r.access_token  # 新浪返回的token，类似abc123xyz456
expires_in = r.expires_in

# 设置得到的access_token~~~~
client.set_access_token(access_token, expires_in)

# 可以打印下看看里面都有什么东西
statuses = client.statuses__friends_timeline()['statuses']  # 获取当前登录用户以及所关注用户（已授权）的微博</span>
length = len(statuses)
print length
# 输出了部分信息
for i in range(0, length):
    print u'昵称：' + statuses[i]['user']['screen_name']
    print u'简介：' + statuses[i]['user']['description']
    print u'位置：' + statuses[i]['user']['location']
    print u'微博：' + statuses[i]['text']

# 'comments api' get the comments of a single weibo
r = client.comments.show.get(id = 2790633513,count = 50,page = 1)

r = client.comments.show.get(id = 2790633513,count = 50,page = 1)
for i in r:
    print i
for st in r.comments:
    text = st.text
    print text