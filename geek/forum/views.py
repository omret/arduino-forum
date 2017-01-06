from django.shortcuts import render
from omretuser.models import User
from .forms import NewTopicForm
from .models import Topic,Comment

# Create your views here.
def forum(request):
    user = __getUserFromSession(request)
    return render(request,'forum/forum.html',{"user":user})

def topic_index(request,index):
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

    return render(request,'forum/topic_index.html',{})

def forum_new(request):
    user = __getUserFromSession(request)
    if user == None:
        return HttpResponseRedirect('/forum/')
    topicform = NewTopicForm()

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
