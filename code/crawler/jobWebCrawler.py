import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait  # WebDriverWait注意大小写
from selenium.webdriver.common.by import By
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

# ----------config-----------
import os
BASE_DIR = os.path.dirname(__file__)
chrome_driver_path = os.path.join(BASE_DIR, "utils/chromedriver_mac64_96")
# ---------------------------

# -----project constants-----
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
}
base_url = "https://www.zhipin.com"
query_template_url = base_url + \
    "/c101020100/?query={query_str}&page={page_num}&ka=page-{page_num}"
description_template_url = base_url+"/wapi/zpgeek/view/job/card.json?jid={jid}&lid={lid}&type=3"
# ---------------------------


options = webdriver.ChromeOptions()
# options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(
    executable_path=chrome_driver_path, chrome_options=options)


driver.get(query_template_url.format(query_str="医药代表", page_num=1))
try:
    job_body = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'job-list')))
except Exception as e:
    print(e)
results = []
job_primarys = job_body.find_elements_by_class_name('job-primary')
for job_primary in job_primarys:
    result = {}
    try:
        job_name_el = job_primary.find_element_by_class_name(
            'job-name').find_element_by_tag_name('a')
        result['jobName'] = job_name_el.text
        result['dataJid'] = job_name_el.get_attribute('data-jid')
        result['dataLid'] = job_name_el.get_attribute('data-lid')

        joblimit = job_primary.find_element_by_class_name('job-limit')
        result['jobSalary'] = joblimit.find_element_by_tag_name('span').text
        other_limit = joblimit.find_element_by_tag_name(
            'p').get_attribute('innerHTML')
        result['jobLimitExperience'], result['jobLimitStudy'] = other_limit.split(
            '<em')[0], other_limit.split('/em>')[-1]
        
        # /wapi/zpgeek/view/job/card.json?jid=" + i + "&lid=" + n + "&type=3"
        try:
            res = requests.get(description_template_url.format(jid=result['dataJid'],lid=result['dataLid']), headers=headers)
            res.raise_for_status()
            res_ob = res.json()
            content = BeautifulSoup(res_ob['zpData']['html'],'lxml')
            job_description = content.find('div',{'class':'detail-bottom-text'})
            result['jobDescription'] = job_description.text if job_description is not None else ""
        except Exception as e:
            print(e)
    except Exception as e:
        print(e)
    results.append(result)
driver.quit()
results = pd.DataFrame(results)
results.to_csv('./data.csv', mode='a', index=False, columns=False)

