import os
import random
from tqdm import tqdm
import time
import json
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait  # WebDriverWait注意大小写
from selenium.webdriver.common.by import By
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

os.chdir(os.path.dirname(__file__))
# ----------config-----------

pc_agent = [
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0);",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
    "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
    "Mozilla/5.0 (X11; Linux x86_64; rv:76.0) Gecko/20100101 Firefox/76.0"
]


base_url = "https://www.zhipin.com"
query_template_url = base_url + \
    "/c101020100/?query={query_str}&page={page_num}&ka=page-{page_num}"
description_template_url = base_url + \
    "/wapi/zpgeek/view/job/card.json?jid={jid}&lid={lid}&type=3"


def get_proxy():
    while True:
        try:
            proxy = requests.get(
                "http://127.0.0.1:5011/get/").json()
            return proxy
        except Exception as e:
            time.sleep(5)


def delete_proxy(proxy):
    requests.get("http://127.0.0.1:5011/delete/?proxy={}".format(proxy))


def getRes(url):
    try_times = 3
    epoch = 0
    while True:
        epoch += 1
        try:
            proxy = get_proxy().get("proxy")
            agent = random.choice(pc_agent)
            headers = {
                'User-Agent': agent
            }
            res = requests.get(url,
                               headers=headers,
                               proxies={"http": "http://{}".format(proxy)},timeout=3000)
            res.raise_for_status()
            code = res.json().get('code')
            if code != 0:
                raise Exception
            # 使用代理访问
            return res
        except Exception as e:
            delete_proxy(proxy)
            time.sleep(random.random()*10)
            print(f"\r失败了，检查一下是不是需要机器人检测{epoch}", "")


# ---------------------------
df = pd.read_csv('./data.csv', header=None)
Jid = df.iloc[1420:, 2]
Lid = df.iloc[1420:, 3]
descs = []
for jid, lid in tqdm(zip(Jid, Lid)):
    desc = {}
    try:
        time.sleep(3+ random.random()*5)
        desc['dataJid'] = jid
        desc['dataLid'] = lid

        res = getRes(description_template_url.format(jid=jid, lid=lid))

        res_ob = res.json()
        content = BeautifulSoup(res_ob['zpData']['html'], 'lxml')
        job_description = content.find('div', {'class': 'detail-bottom-text'})
        desc['jobDescription'] = job_description.text if job_description is not None else ""
    except Exception as e:
        print(e)
        print(jid, lid)

    descs.append(desc)

    if len(descs) == 20:
        descs = pd.DataFrame(descs)
        descs.to_csv('./data_desc.csv', mode='a', index=False,
                     header=False, encoding='utf_8_sig')
        descs = []

descs = pd.DataFrame(descs)
descs.to_csv('./data_desc.csv', mode='a', index=False,
             header=False, encoding='utf_8_sig')
