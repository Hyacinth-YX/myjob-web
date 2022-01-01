from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseBadRequest
import json


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
        return HttpResponse(json.dumps(a))
    else:
        return HttpResponseBadRequest("Not support to such request method")


def tags(requests):
    pass


def personality(requests):
    pass


def wage(requests):
    pass


def major(requests):
    pass


def ageSex(requests):
    pass


def task(requests):
    pass


def hollandCode(requests):
    pass
