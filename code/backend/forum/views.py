from django.middleware.csrf import get_token
import json
from utils.http import HttpWrapper
from utils.errors import NoUser, DuplicateUser, PasswordIncorrect, MethodError
from .models import Post, Comment
from django.forms.models import model_to_dict
# Create your views here.


@HttpWrapper
def getPost(request):
    if request.method == "GET":
        postId = request.GET.get('postId')
        if postId is not None and postId.isnumeric():
            postId = int(postId)
            post = Post.objects.get(id=postId)
            return model_to_dict(post)
        else:
            raise ValueError
    else:
        raise MethodError


@HttpWrapper
def getPosts(request):
    if request.method == "GET":
        jobCat = request.GET.get('jobCat')
        if jobCat is not None and jobCat.isnumeric():
            jobCat = int(jobCat)
            posts = list(Post.objects.filter(jobCat=jobCat).values())
            return posts
        else:
            raise ValueError
    else:
        raise MethodError


@HttpWrapper
def addPost(request):
    if request.method == "POST":
        pass
    else:
        raise MethodError


@HttpWrapper
def getComments(request):
    if request.method == "GET":
        jobId = request.GET.get('jobId')
        if jobId is not None and jobId.isnumeric():
            jobId = int(jobId)
            comment = Comment.objects.get(id=jobId)
            return model_to_dict(comment)
        else:
            raise ValueError
    else:
        raise MethodError


@HttpWrapper
def addComment(request):
    if request.method == "POST":
        pass
    else:
        raise MethodError
