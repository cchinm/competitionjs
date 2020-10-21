# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     pass_mission_1
   Description :
   Author :       zm.z
   date：          2020/10/21
-------------------------------------------------
   Change Activity:
                   2020/10/21:
-------------------------------------------------
"""
__author__ = 'zm.z'

import execjs
import time
import sys
sys.path.append(".")
from scripts.base import BaseFight

class FightMission1(BaseFight):

    def pass_mission(self, url):

        ctx = execjs.compile(open("./hookjs/1.js").read())
        url = "http://match.yuanrenxue.com/api/match/1?page=%d&m="

        headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',

            'Connection': 'keep-alive',
            'Cookie': 'Hm_lvt_9bcbda9cbf86757998a2339a0437208e=1602859196,1603207906,1603208097,1603290531; m=05d82ea0ee54c12bc3536bdb3a8c17ca|1603293739000; Hm_lpvt_9bcbda9cbf86757998a2339a0437208e=1603294031',
            'Host': 'match.yuanrenxue.com',
            'Pragma': 'no-cache',
            'Referer': 'http://match.yuanrenxue.com/match/1',
            'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1',
            'X-Requested-With': 'XMLHttpRequest',
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        for i in range(1, 6):
            s = str(int(time.time()))
            # s = '1603294637'
            m = ctx.call('hex_md5', s + "000")
            m = m + '%E4%B8%A8' + s
            print(url % i + m)

            resp = self.session.get(url=url % i +m,
                                    headers=headers)
            print(resp.json())
            time.sleep(1)


if __name__ == '__main__':
    fm = FightMission1(None, None)
    fm.pass_mission(None)

