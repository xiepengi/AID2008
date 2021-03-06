import re

import execjs
import requests


class BdTranslateSpider():
    def __init__(self):
        self.post_url = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'
        self.post_headers = {
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "zh-CN,zh;q=0.9",
            "content-length": "135",
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "cookie": "BAIDUID=0494F8D75D1CD5904AF3A75D4D08C005:FG=1; BIDUPSID=0494F8D75D1CD5904AF3A75D4D08C005; PSTM=1598595170; BAIDUID_BFESS=C2AA6175403BF4ED84C65190728149AA:FG=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; delPer=0; PSINO=5; H_PS_PSSID=1447_33076_33259_33236_31660_33285_33218_33211_26350_33199_33237_33147_33264; BA_HECTOR=00042g242k2l2181ou1ftgps60r; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1608017801; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1608017810; ab_sr=1.0.0_MTA3NjgxMzYxMjBlMDExNWRlNDIyNjBiYWUxMWRjNGU2ZDRhOTE2N2Q3N2Q0NzRlMThlOTU1OWQ3ZjU1ZmY4YzNlYzJjODdiMzkxNWFiNzAwMGZkYjJlZjI1YWY1NTI0; __yjsv5_shitong=1.0_7_59269d9b34d3f6b1124b5abeb8190fe31467_300_1608017810063_101.81.67.142_71294270; yjs_js_security_passport=31e74563fae71a60a6e148cc8d036936f447ef8d_1608017810_js",
            "origin": "https://fanyi.baidu.com",
            "referer": "https://fanyi.baidu.com/?aldtype=16047",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36",
            "x-requested-with": "XMLHttpRequest",
        }
        self.get_url = 'https://fanyi.baidu.com/'
        self.get_headers = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "zh-CN,zh;q=0.9",
            "cookie": "BAIDUID=0494F8D75D1CD5904AF3A75D4D08C005:FG=1; BIDUPSID=0494F8D75D1CD5904AF3A75D4D08C005; PSTM=1598595170; BAIDUID_BFESS=C2AA6175403BF4ED84C65190728149AA:FG=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; delPer=0; PSINO=5; H_PS_PSSID=1447_33076_33259_33236_31660_33285_33218_33211_26350_33199_33237_33147_33264; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1608017801; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; BA_HECTOR=8g0kalak0g852g2la21ftgupd0r; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1608022951; ab_sr=1.0.0_ZjgyMTY3ZmQ4YjEwZTNmY2QxM2Q4OGFhZjM3YTk0YzQ1ZmQxZmNjZmZjZDM0OGVjZjY1NDFiMjRiMTlkZWUxYTFlNTdiMzU1ZmMxM2NiNTdlMWJkZjJlNzU5OGZmZWY0; __yjsv5_shitong=1.0_7_59269d9b34d3f6b1124b5abeb8190fe31467_300_1608022952317_101.81.67.142_3a6dc758; yjs_js_security_passport=da0e575e1d4d0f15d1583a66bee5efd2c8f445bc_1608022956_js",
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "none",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36",
        }

    def get_gtk_token(self):
        html = requests.get(url=self.get_url, headers=self.get_headers).text
        gtk = re.findall("window.gtk = '(.*?)'", html, re.S)[0]
        token = re.findall("token: '(.*?)'", html, re.S)[0]

        return gtk, token

    def get_sign(self, word):
        gtk, token = self.get_gtk_token()
        # 获取sign: 利用execjs模块
        with open('translate.js', 'r') as f:
            jscode = f.read()
            js_obj = execjs.compile(jscode)
            sign = js_obj.eval('e("{}", "{}")'.format(word, gtk))
            return sign

    def attack_bd(self, word):
        """爬虫逻辑函数"""
        gtk, token = self.get_gtk_token()
        sign = self.get_sign(word)
        data = {
            "from": "en",
            "to": "zh",
            "query": word,
            "transtype": "realtime",
            "simple_means_flag": "3",
            "sign": sign,
            "token": token,
            "domain": "common",
        }
        html = requests.post(url=self.post_url, data=data, headers=self.post_headers).json()
        print(html)

    def crawl(self):
        word = input("请输入要查询的单词:")
        self.attack_bd(word)


if __name__ == '__main__':
    spider = BdTranslateSpider()
    spider.crawl()
