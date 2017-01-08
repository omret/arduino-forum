from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from omretuser.models import User
from .forms import NewTopicForm
from qiniu import Auth, put_file
import qiniu.config
from geek import settings
import json
from .models import Topic,Comment

ACCESS_KEY = settings.ACCESS_KEY
SECRET_KEY = settings.SECRET_KEY
BUKET_NAME = settings.BUKET_NAME

# Create your views here.
def forum(request):
    user = __getUserFromSession(request)
    topic_list = Topic.objects.all()
    paginator = Paginator(topic_list, 10)
    page = request.GET.get('page')

    try:
        topices = paginator.page(page)
    except PageNotAnInteger:
        topices = paginator.page(1)
    except EmptyPage:
        topices = paginator.page(paginator.num_pages)

    topic_dict = {}
    for topic in topices:
        comment_num = Comment.objects.filter(topic=topic).count()
        topic_dict[topic]=comment_num
    return render(request,'omretforum/forum.html',{"user":user,"topic_dict":topic_dict,"topices":topices})

def topic_index(request,index):
    print(request.path)
    user = __getUserFromSession(request)
    try:
        topic = Topic.objects.get(id=index)
    except Exception as e:
        return HttpResponseRedirect('/')
        print(e)
    try:
        topic_comment = Comment.objects.get(topic=topic)
    except Exception as e:
        topic_commnet = None

    return render(request,'omretforum/topic_index.html',{"user":user,"topic":topic,"nextpath":request.path})

def forum_new(request):
    user = __getUserFromSession(request)
    if user == None:
        return HttpResponseRedirect('/')
    topicform = NewTopicForm()
    if request.method == "POST":
        topicformPost = NewTopicForm(request.POST)
        if topicformPost.is_valid():
            title = topicformPost.cleaned_data['title']
            content = topicformPost.cleaned_data['content']
            newtopic = Topic()
            __setNewTopic(newtopic,title,content,user)
            try:
                newtopic.save()
                return HttpResponseRedirect('/')
            except Exception as e:
                print(e)
    response = render(request,'omretforum/forumnew.html',{"user":user,"topicform":topicform})
    return response

def __getUserFromSession(request):
    try:
        uid = request.session.get('uid')
        user = User.objects.get(id=uid)
        return user
    except Exception as e:
        print (e)
        return None

def __setNewTopic(newtopic,title,content,user):
    newtopic.title = title
    newtopic.content = content
    newtopic.author = user

#qiniu token
def token(req):
    q = Auth(ACCESS_KEY, SECRET_KEY)

    # key = uuid.uuid1()
    # print BUKET_NAME
    token = q.upload_token(BUKET_NAME)

    return HttpResponse(json.dumps({"uptoken": token}))
