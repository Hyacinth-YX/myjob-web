import requests
import itertools
from zhconv import convert
import pandas as pd
import numpy as np

headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    }
def get_data(url):
    r = requests.get(url,headers = headers)
    res = r.json()['data']
    return res

def main():

    df = pd.DataFrame(
        columns=['bigJobImg', 'holland1', 'holland2', 'holland3', 'jobCat', 'jobDesc', 'jobName', 'jobWorks',
                 'subject1', 'subject2'])
    failed = []
    df_related = pd.DataFrame(columns = ['jobCat','relatedJob'])
    for i in itertools.permutations('RIASEC', 3):
        try:

            print(i[0])
            url = 'https://wow.104.com.tw/gt/career/list/type/' + i[0] + '/' + i[1] + '/' + i[2]
            res = get_data(url)
            print(res)
            print(i)
            for job in range(len(res)):
                print(job)
                print(res[job])
                fields = list(res[job].keys())
                bigJobImg = res[job]['bigJobImg']
                holland1 = ''
                holland2 = ''
                holland3 = ''
                if 'holland1' in fields:
                    holland1 = res[job]['holland1']
                if 'holland2' in fields:
                    holland2 = res[job]['holland2']
                if 'holland3' in fields:
                    holland3 = res[job]['holland3']
                jobCat = res[job]['jobCat']
                jobDesc = convert(res[job]['jobDesc'],'zh-cn')
                jobName = convert(res[job]['jobName'],'zh-cn')
                jobWorks = convert(res[job]['jobWorks'],'zh-cn')
                subject1 = ''
                subject2 = ''
                relatedJob1 = ''
                relatedJob2 = ''
                if 'subject1' in fields:
                    subject1 = res[job]['subject1']

                if 'subject2' in fields:
                    subject2 = res[job]['subject2']
                df = df.append({'bigJobImg':bigJobImg, 'holland1':holland1, 'holland2':holland2, 'holland3':holland3, 'jobCat':jobCat, 'jobDesc':jobDesc, 'jobName':jobName, 'jobWorks':jobWorks,
                     'subject1':subject1, 'subject2':subject2},ignore_index=True)
                if 'relatedJob1' in fields:
                    relatedJob1 = res[job]['relatedJob1']
                if 'relatedJob2' in fields:
                    relatedJob2 = res[job]['relatedJob2']

                df_related = df_related.append({'JobCat': jobCat, 'relatedJob': relatedJob1},ignore_index=True)
                df_related = df_related.append({'JobCat': jobCat, 'relatedJob': relatedJob2},ignore_index=True)
        except:
            failed.append(i)

    print(failed)
    df.to_csv('./104hollland.csv',encoding ='utf_8_sig')
    df_related.to_csv('./relatedjob.csv',encoding = 'utf_8_sig')

main()