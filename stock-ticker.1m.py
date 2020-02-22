#!/usr/bin/env PYTHONIOENCODING=UTF-8 /usr/local/anaconda3/bin/python3
# <bitbar.title>Stock Ticker</bitbar.title>
# <bitbar.version>1.0</bitbar.version>
# <bitbar.author>Robert Kanter</bitbar.author>
# <bitbar.author.github>rkanter</bitbar.author.github>
# <bitbar.desc>Provides a rotating stock ticker in your menu bar, with color and percentage changes</bitbar.desc>
# <bitbar.dependencies>python</bitbar.dependencies>
# <bitbar.image>https://i.imgur.com/Nf4jiRd.png</bitbar.image>
# <bitbar.abouturl>https://github.com/rkanter</bitbar.abouturl>

from urllib.request import urlopen, Request
import json
import time

# 配置想要显示的股票
stock_codes = ['s_sh000001', 's_sz399300']

# -----------------------------------------------------------------------------
t = time.localtime()
day, hour, minuten, second = t.tm_wday, t.tm_hour, t.tm_min, t.tm_sec

red = '#F73C2E'
green = '#33bd59'
black = '#87878b'


if (hour != 14 or day == 5 or day == 6):
    # print("恭喜发财 | color=#F73C2E")

    print("每日佳句")

    print("---")

    r = Request('https://api.ooopn.com/ciba/api.php?type=json', headers={
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1 Safari/605.1.15'})
    response = json.loads(urlopen(r).read())

    print("{} | color=red".format(response["ciba-en"]))

    print(response["ciba"])

    exit()
    pass

if minuten % 2:
    stock_codes = stock_codes[::-1]
    pass

stock_codes_str = ','.join(stock_codes)

r = Request('http://hq.sinajs.cn/list='+stock_codes_str, headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1 Safari/605.1.15'})
response = str(urlopen(r).read().decode(
    'gbk').encode("utf-8"), encoding='utf-8')

stocks = response.split(';')

for index in range(len(stock_codes)):
    stock = stocks[index]
    name, index, _, change_percent, _, _ = stock.split('"')[1].split(',')

    change_percent = float(change_percent)
    if change_percent != 0:
        color = red if change_percent > 0 else green
        print("{} {:.2f} ({:.2f}%) | color={}".format(
            name, float(index), change_percent, color))
    else:
        color = black
        print("{} {:.2f} | color={}".format(name, float(index), color))
