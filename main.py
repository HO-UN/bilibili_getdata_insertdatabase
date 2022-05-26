import requests  # 用于得到网页链接

import time  # 用于程序延时
import json  # 用于解析JSON格式的库

# B站UP主UID

uid = '2303936'
ck = open("cookies.txt").read()

def cookie_to_dic(cookie):
    return {item.split('=')[0]: item.split('=')[1] for item in cookie.split('; ')}

def get_fans(fanuid):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0'}
    # 储存粉丝数
    response = requests.get('https://api.bilibili.com/x/relation/stat?vmid=' + fanuid + '&jsonp=jsonp',
                            headers=headers)
    J_data = json.loads(response.text)
    return J_data['data']['follower']

def get_data(page):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Connection': 'keep-alive'}
    params = {'vmid': uid,
              'pn': page,  # 页数
              'ps': '30',
              'order': 'desc',
              'order_type': 'attention',
              'jsonp': 'jsonp',
              }
    cookies= cookie_to_dic(ck)
    response = requests.get('http://api.bilibili.com/x/relation/followings?vmid=' + uid,
                            headers=headers,
                            params=params,
                            cookies=cookies)

    jdata = json.loads(response.text)
    # for i in range(1, 21):
    #     if jdata['data']['list'][i]['attribute'] == 6 and get_fans(str(jdata['data']['list'][i]['mid']))>=1000:
    #         neo4j_join( str(jdata['data']['list'][i]['uname']),str(jdata['data']['list'][i]['sign']),str(str(jdata['data']['list'][i]['face']).strip('http://i2.hdslb.com/bfs/face/')
    #                     .strip('0.hdslb.com/bfs/face/').strip('1.hdslb.com/bfs/face/')))

    with open('fansdata1.txt', 'a', encoding='utf-8') as f:
        for i in range(1, 21):
            if jdata['data']['list'][i]['attribute'] == 6 and get_fans(str(jdata['data']['list'][i]['mid']))>1000:
                f.write(str(str(jdata['data']['list'][i]['face']).strip('http://i2.hdslb.com/bfs/face/')
                            .strip('0.hdslb.com/bfs/face/').strip('1.hdslb.com/bfs/face/') + '\n'))
    with open('onlyarr1.txt', 'a', encoding='utf-8') as f:
        for i in range(1, 21):
            if jdata['data']['list'][i]['attribute'] == 6 and get_fans(str(jdata['data']['list'][i]['mid']))>1000:
                f.write(str(str(jdata['data']['list'][i]['face'])+ '\n'))
    # with open('uid1.txt', 'a', encoding='utf-8') as f:
    #     for i in range(1, 21):
    #         if jdata['data']['list'][i]['attribute'] == 6 and get_fans(str(jdata['data']['list'][i]['mid']))>1000:
    #             f.write(str(jdata['data']['list'][i]['mid'])+'\n')
    # with open('name1.txt', 'a', encoding='utf-8') as f:
    #     for i in range(1, 21):
    #         if jdata['data']['list'][i]['attribute'] == 6 and get_fans(str(jdata['data']['list'][i]['mid']))>1000:
    #             f.write(str(jdata['data']['list'][i]['uname'])+'\n')

def main():
    for page in range(1,65):      #粉丝页数
        get_data(page)
        time.sleep(1)

if __name__ == '__main__':
    main()
