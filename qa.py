# encoding:UTF-8

'''
python interpreter version: 3.6
Code a crawler to access data.
You could get the identical weibo_id from every single weibo.
The hotest comments or newest comments of this weibo could be returned.
In this code, only the comments targeting replying others are recorded and write down to local files
'''

import re,time,requests,urllib.request

# weibo_id = input('输入单条微博ID：')
weibo_id = '4139105182563592'
print('weibo_id = ' + weibo_id)
# url='https://m.weibo.cn/single/rcList?format=cards&id=' + weibo_id + '&type=comment&hot=1&page={}' #爬热门评论
url='https://m.weibo.cn/api/comments/show?id=' + weibo_id + '&page={}' #爬时间排序评论
headers = {
    'User-agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
    'Host' : 'm.weibo.cn',
    'Accept' : 'application/json, text/plain, */*',
    'Accept-Language' : 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding' : 'gzip, deflate, br',
    'Referer' : 'https://m.weibo.cn/status/' + weibo_id,
    'Cookie' : '登录cookie信息',
    'DNT' : '1',
    'Connection' : 'keep-alive',
    }
i = 0
comment_num = 1

f1 = open('qaSet.txt', 'a+', encoding='utf-8')
# f2 = file('val', 'a+')
# f3 = open('train', 'a+')
# j = int(0)
# for line in f1:
#     if j < 40:
#         f2.write(line)
#         j += 1
#         # f3.write(line)
# f2.flush()
# f3.flush()
# f1.close()
# f2.close()
# f3.close()

while True:
    # if i==1:     #爬热门评论
    #     r = requests.get(url = url.format(i),headers = headers)
    #     comment_page = r.json()[1]['card_group']
    # else:
    #     r = requests.get(url = url.format(i),headers = headers)
    #     comment_page = r.json()[0]['card_group']
    r = requests.get(url = url.format(i),headers = headers)  #爬时间排序评论
    comment_page = r.json()['data']
    if r.status_code ==200:
        try:
            # print('正在读取第 %s 页评论：' % i)
            for j in range(0,len(comment_page)):
                user = comment_page[j]
                if 'reply_id' in user:
                    print('reply_id', user['reply_id'])
                    reply_text = re.sub('<.*?>|回复<.*?>:|[\U00010000-\U0010ffff]|[\uD800-\uDBFF][\uDC00-\uDFFF]', '',
                                  user['reply_text'])
                    print('reply_text', reply_text)
                    print('id', user['user']['id'])
                    text = re.sub('<.*?>|回复<.*?>:|[\U00010000-\U0010ffff]|[\uD800-\uDBFF][\uDC00-\uDFFF]', '',
                                  user['text'])
                    print('text', text + '\n')
                    f1.write(str(user['reply_id'])+ '\t' + reply_text + '\t' + str(user['user']['id']) + '\t' + text + '\n')
                    f1.flush()

                    # print('第 %s 条评论' % comment_num)

                    # comment_id = user['user']['id']
                    # print(comment_id)
                    # user_name = user['user']['screen_name']
                    # print(user_name)
                    # created_at = user['created_at']
                    # print(created_at)
                    #
                    # likenum = user['like_counts']
                    # print(likenum)
                    # source = re.sub('[\U00010000-\U0010ffff]|[\uD800-\uDBFF][\uDC00-\uDFFF]','',user['source'])
                    # print(source + '\r\n')
                    comment_num+=1
            i+=1
            # time.sleep(3)
        except Exception as e:
            print(e)
            # i+1
            pass
    else:
        break