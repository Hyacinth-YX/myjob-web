from bs4.element import ResultSet
from django.http.response import HttpResponseServerError
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseBadRequest
import json
import numpy as np
import pandas as pd
from numpy.core.fromnumeric import trace
from zhconv import convert
import requests as req
from .models import HollandQuestions


def jobs(requests: HttpRequest):
    if requests.method == "GET":
        a = {
            "jobCat": "2005003008",
            "bigJobImg": "https://static.104.com.tw/gtnew/img/character/bigRole/2005003008.png",
            "jobName": "醫藥業務代表",
            "jobDesc": "我會把藥賣出去，推廣客戶需要的醫療產品！",
            "jobWorks": "拜訪固定或非固定地區醫院、診所、藥局客戶，以開發或維護客戶關係。\n銷售及推廣公司產品，例如醫療研究用儀器或醫藥耗材等。\n教育及示範產品使用方式。\n協助客戶使用產品。\n提供新客戶相關之行銷或經營輔導。\n宣導與執行公司的理念予店家。",
            "subject1": "social",
            "subject2": "biology"
        }
        zh_result = {k: convert(v, 'zh-cn') for k, v in a.items()}
        return HttpResponse(json.dumps(zh_result))
    else:
        return HttpResponseBadRequest("Not support to such request method")


def tags(requests: HttpRequest):
    """
    https://www.104.com.tw/jb/jobwiki/jobCatMaster/tagCloudJSON?jobcat=2005003008&type=1%2C2%2C3%2C4
    """
    if requests.method == "GET":
        jobcat = requests.GET.get('jobCat')
        template_url = "https://www.104.com.tw/jb/jobwiki/jobCatMaster/tagCloudJSON?jobcat={}&type=1%2C2%2C3%2C4"
        try:
            if jobcat is None:
                res_ob = {}
            else:
                res = req.get(template_url.format(jobcat))
                res.raise_for_status()
                res_ob = res.json()
            result = {}
            for kind in ['certification', 'skill', 'tool']:
                result[kind] = [{'desc': convert(row.get('funDesc'), 'zh-cn'),
                                 'count': row.get('count')}
                                for row in res_ob.get(kind)]
            return HttpResponse(json.dumps(result))
        except Exception as e:
            return HttpResponseServerError(str(e))
    else:
        return HttpResponseBadRequest("Not support to such request method")


def personality(requests):
    """
    example: https://www.104.com.tw/jb/jobwiki/jobCatMaster/personality?jobcat=2005003008
    """
    personality_template_url = "https://www.104.com.tw/jb/jobwiki/jobCatMaster/personality?jobcat=2005003008"
    if requests.method == "GET":
        jobcat = requests.GET.get('jobCat')
        template_url = "https://www.104.com.tw/jb/jobwiki/jobCatMaster/personality?jobcat={}"
        try:
            if jobcat is None:
                res_ob = {}
            else:
                res = req.get(template_url.format(jobcat))
                res.raise_for_status()
                res_ob = res.json()
            result = res_ob.get('big5')
            return HttpResponse(json.dumps(result))
        except Exception as e:
            return HttpResponseServerError(str(e))
    else:
        return HttpResponseBadRequest("Not support to such request method")


def wage(requests):
    """
    TODO: Use local data
    """
    if requests.method == "GET":
        jobcat = requests.GET.get('jobCat')

        try:
            pass
        except Exception as e:
            return HttpResponseServerError(str(e))
    else:
        return HttpResponseBadRequest("Not support to such request method")


def major(requests):
    """
    https://www.104.com.tw/jb/jobwiki/jobCatMaster/major?jobcat=2005003008&top=50
    """
    if requests.method == "GET":
        jobcat = requests.GET.get('jobCat')
        top = requests.GET.get('top')
        top = top if top is not None else 50
        template_url = "https://www.104.com.tw/jb/jobwiki/jobCatMaster/major?jobcat={}&top={}"
        try:
            if jobcat is None:
                res_ob = {}
            else:
                res = req.get(template_url.format(jobcat, top))
                res.raise_for_status()
                res_ob = res.json()
            result = [{'majorName': convert(row.get('majorName'), 'zh-cn'),
                       'count': row.get('count')} for row in res_ob.get('majors')]
            return HttpResponse(json.dumps(result))
        except Exception as e:
            return HttpResponseServerError(str(e))
    else:
        return HttpResponseBadRequest("Not support to such request method")


def ageSex(requests):
    """
    https://www.104.com.tw/jb/jobwiki/jobCatMaster/bmi?jobcat=2005003008
    """
    if requests.method == "GET":
        jobcat = requests.GET.get('jobCat')
        top = requests.GET.get('top')
        top = top if top is not None else 50
        template_url = "https://www.104.com.tw/jb/jobwiki/jobCatMaster/bmi?jobcat={}"
        try:
            if jobcat is None:
                res_ob = {}
            else:
                res = req.get(template_url.format(jobcat, top))
                res.raise_for_status()
                res_ob = res.json()
            result = {}
            for k, v in res_ob.items():
                if isinstance(v, dict):
                    result[k] = {
                        'male': v.get('male'),
                        'female': v.get('female')
                    }
            return HttpResponse(json.dumps(result))
        except Exception as e:
            return HttpResponseServerError(str(e))
    else:
        return HttpResponseBadRequest("Not support to such request method")


def task(requests):
    """
    https://www.104.com.tw/jb/jobwiki/jobCatMaster/task?jobcat=2005003008
    """
    if requests.method == "GET":
        jobcat = requests.GET.get('jobCat')
        top = requests.GET.get('top')
        top = top if top is not None else 50
        template_url = "https://www.104.com.tw/jb/jobwiki/jobCatMaster/bmi?jobcat={}"
        try:
            if jobcat is None:
                res_ob = {}
            else:
                res = req.get(template_url.format(jobcat, top))
                res.raise_for_status()
                res_ob = res.json()
            result = {'content': convert(res_ob.get('content'), 'zh-cn'),
                      'missions': [convert(v, 'zh-cn') for v in res_ob.get('missions')]}
            return HttpResponse(json.dumps(result))
        except Exception as e:
            return HttpResponseServerError(str(e))
    else:
        return HttpResponseBadRequest("Not support to such request method")


def get_holland(ans: list):
    ans = np.array(ans).reshape(15, 6)
    ans = pd.DataFrame(ans)
    lst = ["R", "I", "A", "S", "E", "C"]
    ans.columns = lst
    ans.loc['total_grade'] = ans.apply(lambda x: x.sum())
    ans = ans.sort_values(by='total_grade', axis=1, ascending=False)
    t = list(ans.columns)
    return t[:3]


def hollandCode(requests):
    if requests.method == "POST":
        post_body = json.loads(requests.body)
        holland_answer = post_body.get('hollandAnswer')
        if holland_answer is None:
            return HttpResponseBadRequest('No Key name hollandAnswer')
        holland_code = get_holland(holland_answer)
        result = {
            'key1': holland_code[0],
            'key2': holland_code[1],
            'key3': holland_code[2]
        }
        return HttpResponse(json.dumps(result))
    else:
        return HttpResponseBadRequest("Not support to such request method")


def hollandCodeQuestions(requests):
    if requests.method == "GET":
        start_index = requests.GET.get('startIndex') if requests.GET.get(
            'startIndex') is not None else 0
        number = requests.GET.get('number') if requests.GET.get(
            'number') is not None else 1
        try:
            start_index, number = int(start_index), int(number)
        except:
            return HttpResponseBadRequest("Not support value of startIndex, number")
        result = HollandQuestions.questions[start_index:start_index+number]
        return HttpResponse(json.dumps(result))
    else:
        return HttpResponseBadRequest("Not support to such request method")
