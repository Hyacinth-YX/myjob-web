from pickle import NONE
from django.http.response import HttpResponseServerError
from django.http import HttpResponse, HttpRequest, HttpResponseBadRequest
from django.forms.models import model_to_dict
import json
import numpy as np
import pandas as pd
from zhconv import convert
import requests as req
from .models import HollandQuestions, BigJob, Job
from utils.http import HttpWrapper
from utils.errors import MethodError, NoValue
import os
from utils.utils import salary_parse
from backend.settings import BASE_DIR
import random
os.chdir(os.path.dirname(__file__))


@HttpWrapper
def jobs(requests: HttpRequest):
    if requests.method == "GET":
        keys = (requests.GET.get('key1'),
                requests.GET.get('key2'),
                requests.GET.get('key3'))
        limit = int(requests.GET.get('limit')) if requests.GET.get(
            'limit').isnumeric() else None
        options = {'holland1__in': keys,
                   'holland2__in': keys,
                   'holland3__in': keys}
        result = list(BigJob.objects.filter(**options).values())
        if limit is not None:
            result = result[:limit]
        return result
    else:
        raise MethodError

@HttpWrapper
def allBigJobs(requests: HttpRequest):
    if requests.method == "GET":
        limit = int(requests.GET.get('limit')) if requests.GET.get(
            'limit') is not None and requests.GET.get('limit').isnumeric() else None
        if requests.GET.get('useCache') is None:
            result = list(BigJob.objects.all().values())
            for o in result:
                try:
                    resultSet = list(Job.objects.filter(jobName=o['jobName']).values())
                    daily_salary = [salary_parse(o.get('jobSalary'))for o in resultSet]
                    daily_salary = [v for v in daily_salary if v > 0]
                    if len(daily_salary) > 0:
                        daily_salary = sum(daily_salary)/len(daily_salary)
                    else:
                        daily_salary = 100000
                    o['salary'] = daily_salary
                except Exception as e:
                    print(e)
            result.sort(key=lambda x: x.get('salary'),reverse=True)
            with open(os.path.join(BASE_DIR, 'data/bigjobsCache.json'),'w') as f:
                f.write(json.dumps(result))
        else:
            with open(os.path.join(BASE_DIR, 'data/bigjobsCache.json'), 'r') as f:
                result = json.loads(f.read())
        if limit is not None:
            result = result[:limit]
        return result
    else:
        raise MethodError


related_job = pd.read_csv(os.path.join(BASE_DIR, 'data/relatedjob.csv'))
related_job = related_job.dropna().drop_duplicates().astype(int)


@HttpWrapper
def releventJob(requests: HttpRequest):
    if requests.method == "GET":
        jobcat = requests.GET.get('jobCat')
        if jobcat is not None and jobcat.isnumeric():
            jobcat = int(jobcat)
            return related_job['JobCat' == jobcat].relatedJob.to_numpy().tolist()
        else:
            return []
    else:
        raise MethodError


@HttpWrapper
def jobdetail(requests: HttpRequest):
    if requests.method == "GET":
        jobId = requests.GET.get('jobId')
        if jobId is not None and jobId.isnumeric():
            jobId = int(jobId)
            ob = Job.objects.get(id=jobId)
            return model_to_dict(ob)
        else:
            return {}
    else:
        raise MethodError


@HttpWrapper
def bigjobSalaryTrend(requests: HttpRequest):
    if requests.method == "GET":
        jobcat = requests.GET.get('jobCat')
        big_ob = BigJob.objects.get(jobCat=jobcat)
        resultSet = list(Job.objects.filter(jobName=big_ob.jobName).values())
        daily_salary = [salary_parse(o.get('jobSalary'))for o in resultSet]
        daily_salary = [v for v in daily_salary if v > 0]
        if len(daily_salary) > 0:
            daily_salary = sum(daily_salary)/len(daily_salary)
        else:
            daily_salary = 100000
        start_date = (2010, 1)
        end_date = (2022, 1)
        result = []
        for year in range(end_date[0], start_date[0]-1, -1):
            for month in range(12, 0, -1):
                result.append({
                    "Date": str(year) + '-' + str(month),
                    "scales": daily_salary
                })
                daily_salary += (random.random()-0.8)*30*10
        result.reverse()
        return result
    else:
        raise MethodError


@HttpWrapper
def jobSalaryTrend(requests: HttpRequest):
    if requests.method == "GET":
        pass
    else:
        raise MethodError


@HttpWrapper
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
            return result
        except Exception as e:
            raise e
    else:
        raise MethodError


@HttpWrapper
def personality(requests):
    """
    example: https://www.104.com.tw/jb/jobwiki/jobCatMaster/personality?jobcat=2005003008
    """
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
            return result
        except Exception as e:
            raise e
    else:
        raise MethodError


@HttpWrapper
def wage(requests):
    """
    TODO: Use local data
    """
    if requests.method == "GET":
        jobcat = requests.GET.get('jobCat')
        try:
            return ""
        except Exception as e:
            raise e
    else:
        raise MethodError


@HttpWrapper
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
            return result
        except Exception as e:
            raise e
    else:
        raise MethodError


@HttpWrapper
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
            return result
        except Exception as e:
            raise e
    else:
        raise MethodError


@HttpWrapper
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
            return result
        except Exception as e:
            raise e
    else:
        raise MethodError


def get_holland(ans: list):
    ans = np.array(ans).reshape(15, 6)
    ans = pd.DataFrame(ans)
    lst = ["R", "I", "A", "S", "E", "C"]
    ans.columns = lst
    ans.loc['total_grade'] = ans.apply(lambda x: x.sum())
    ans = ans.sort_values(by='total_grade', axis=1, ascending=False)
    t = list(ans.columns)
    return t[:3]


@HttpWrapper
def hollandCode(requests):
    if requests.method == "POST":
        post_body = json.loads(requests.body)
        holland_answer = post_body.get('hollandAnswer')
        if holland_answer is None:
            raise NoValue('body no key hollandAnswer')
        holland_code = get_holland(holland_answer)
        result = {
            'key1': holland_code[0],
            'key2': holland_code[1],
            'key3': holland_code[2]
        }
        return result
    else:
        raise MethodError


@HttpWrapper
def hollandCodeQuestions(requests):
    if requests.method == "GET":
        start_index = requests.GET.get('startIndex') if requests.GET.get(
            'startIndex') is not None else 0
        number = requests.GET.get('number') if requests.GET.get(
            'number') is not None else 1
        try:
            start_index, number = int(start_index), int(number)
        except:
            raise ValueError("Not support value of startIndex, number")
        result = HollandQuestions.questions[start_index:start_index+number]
        return result
    else:
        raise MethodError
