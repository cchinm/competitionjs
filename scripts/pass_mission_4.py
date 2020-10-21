# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     pass_mission_4
   Description : 雪碧图
   Author :       zm.z
   date：          2020/10/16
-------------------------------------------------
   Change Activity:
                   2020/10/16:
-------------------------------------------------
"""
import hashlib
import re
from pprint import pprint

import execjs

__author__ = 'zm.z'

from scripts.base import BaseFight
import lxml.html
from base64 import b64decode, b64encode

md5_digital = {'1257ee3fd8f34b39c7f606a768790fcd': '9',
 '140555df4c741e5c4d5716fbd9c737e8': '5',
 '4bf96e6e3d15bcca18404d1ca0951b9b': '8',
 '52c0d13d7b4008445798d0ab9f8dc374': '2',
 '53f03ba24510bd8d162a11d8cd9755d2': '4',
 '6043fb378ad2e43897968cde6a219a8b': '7',
 '84167d3bdfb936ac7d0e4099fc036815': '6',
 '9cb54eee0868b1b37d43471fcce12dea': '3',
 'f1e4a91211fbc109d79ad8ab0ae0e66a': '0'}

class FightMission4(BaseFight):

    def pass_mission(self, url):

        page_url = 'http://match.yuanrenxue.com/api/match/4?page='
        # page_url = url

        img_split_xpath = '//td'
        img_src = './img/@src'
        img_class = './img/@class'
        img_stype = './img/@style'

        result = 0

        for page in range(1, 6):


            resp = self.session.get(url=page_url + str(page)).json()
            doc = lxml.html.fromstring(resp['info'])
            tds = doc.xpath(img_split_xpath)

            display_label = self._md5(b64encode((resp['key']+resp['value']).encode()).decode().replace("=", ""))
            print(display_label, resp['key']+resp['value'])
            print(page_url, page)
            for i, td in enumerate(tds):
                print("part ", i)
                img_src_list = td.xpath(img_src)
                img_class_list = td.xpath(img_class)
                img_stype_list = td.xpath(img_stype)

                img_tuple = []
                for x, y, z in zip(img_class_list, img_src_list, img_stype_list):

                    if x.find(display_label) > -1:continue
                    img_tuple.append((self._re(z), self._md5(y)))
                print(self.sort(*img_tuple))
                result += int(self.sort(*img_tuple))

        print(result)


    def _md5(self, s):
        print(s[-20:])
        m = hashlib.md5()
        m.update(s.encode())
        print(m.hexdigest())
        return m.hexdigest()

    def _re(self, s):

        c = re.compile('left:(.+)px')
        return int(c.search(s).group(1))

    def sort(self, *args):

        s = ['', ] * len(args)
        for i, val in enumerate(args):
            _i = val[0] % 11

            s[_i+i] = md5_digital.get(val[1], '1')

        return "".join(s)



if __name__ == '__main__':

    f4 = FightMission4()
    f4.login()
    f4.pass_mission(11)
