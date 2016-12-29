from django.shortcuts import render
from omretuser.models import User
from .forms import NewTopicForm

# Create your views here.
def forum(request):
    user = __getUserFromSession(request)
    return render(request,'forum/forum.html',{"user":user})

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
