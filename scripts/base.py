# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     base
   Description :
   Author :       zm.z
   date：          2020/10/16
-------------------------------------------------
   Change Activity:
                   2020/10/16:
-------------------------------------------------
"""
import requests

__author__ = 'zm.z'

class BaseFight:


    def __init__(self, user, password):

        self.user = user
        self.password = password
        self.cookies = None
        self.session = requests.Session()
        # self.login()

    def login(self):

        prepare_url = 'http://match.yuanrenxue.com/api/loginInfo'
        url = 'http://match.yuanrenxue.com/api/login'
        headers = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',

            'Content-Type': 'application/x-www-form-urlencoded',
            'Cookie': 'Hm_lvt_9bcbda9cbf86757998a2339a0437208e=1602770260,1602850733; RM4hZBv0dDon443M=PAhCeooj6QPyrUTXf2VQMSRQYPSl2b1gintInso5hI5AmcwHNKUqg1v91LFL1d9EDBMYWSoNDQCLwqHjgIuKYBK5nygBWQt+n3lucXw5tKXDnpsjMUPXyYEPt+0PFkQJtRN4bXMgIJ8QVrVqbouNFv6n8QQI3f+1n20RD+wt6p1tX0Jsu4dAZ8UhgCRbPatpyvL+kT8RGoFgr+aZa2vjIdwDPkcdhy9T7GAMi6BCSXY=; m=155; tk=19447229490229590; Hm_lpvt_9bcbda9cbf86757998a2339a0437208e=1602859021',
            'Host': 'match.yuanrenxue.com',
            'Origin': 'http://match.yuanrenxue.com',
            'Pragma': 'no-cache',
            'Referer': 'http://match.yuanrenxue.com/login',
            'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1',
            'X-Requested-With': 'XMLHttpRequest'
        }
        self.session.get(url=url)
        self.session.get(url=prepare_url)

        resp = self.session.post(url=url,
                          headers=headers,
                          data=dict(username=self.user,
                                    password=self.password))
        resp.raise_for_status()
        print(resp.json())
        assert resp.json()['status_code'] == '1', "登录失败"
        print("登录成功")
        self.cookies = resp.cookies.get_dict()


    def pass_mission(self, url):
        raise NotImplementedError