from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from omretuser.models import User
from .forms import NewTopicForm
from .models import Topic

from qiniu import Auth, put_file
import qiniu.config
from geek import settings

ACCESS_KEY = settings.ACCESS_KEY
SECRET_KEY = settings.SECRET_KEY
BUKET_NAME = settings.BUKET_NAME

# Create your views here.
def forum(request):
    user = __getUserFromSession(request)
    return render(request,'forum/forum.html',{"user":user})

def forum_new(request):
    user = __getUserFromSession(request)
    if user == None:
        return HttpResponseRedirect('/forum/')
    topicform = NewTopicForm()
    if request.method == "POST":
        topicformPost = NewTopicForm(request.POST)
        if topicformPost.is_valid():
            title = topicformPost.cleaned_data['title']
            content = topicformPost.cleaned_data['content']
            newtopic = Topic()
            __setNewTopic(newtopic,title,content,user)
            try:
                newsarti.save()
                return HttpResponseRedirect('/forum/')
            except Exception as e:
                print(e)
    response = render(request,'forum/forumnew.html',{"user":user,"topicform":topicform})
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
