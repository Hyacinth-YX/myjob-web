from utils.http import HttpWrapper
from utils.errors import *
from .models import jobRecord


@HttpWrapper
def recordJob(request):
    if request.method == "GET":
        jobId = request.GET.get('jobId')
        uid = request.GET.get('uid')
        if uid is not None and jobId is not None:
            ob = jobRecord.objects.create(uid=uid, jobId=jobId)
            ob.save()
            return {'result': 'success'}
        else:
            raise KeyError
    else:
        raise MethodError


@HttpWrapper
def recommendJob(request):
    if request.method == "GET":
        pass
    else:
        raise MethodError


@HttpWrapper
def recordBigjob(request):
    raise NotImplementedError
