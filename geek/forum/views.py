from django.shortcuts import render
from omretuser.models import User

# Create your views here.
def forum(request):
    user = __getUserFromSession(request)
    return render(request,'forum/forum.html',{"user":user})

def __getUserFromSession(request):
    try:
        uid = request.session.get('uid')
        user = User.objects.get(id=uid)
        return user
    except Exception as e:
        print (e)
        return None
