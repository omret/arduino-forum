from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect,csrf_exempt

import json
import hashlib
import uuid

from .models import User

# Create your views here.
def signup(request):
    nextpath = request.GET.get('next')
    return render(request,'omretuser/signup.html',{'nextpath':nextpath})

@csrf_protect
def signup_submit(request):
    nextpath = request.GET.get('next')
    if request.method == 'POST':
        username = request.POST.get("username","")
        email = request.POST.get("email","")
        password = request.POST.get("password","")

        if (username.strip() and email.strip() and password.strip()) != '' :
            user = User()
            user.name = username
            user.email = email
            print(hashlib.sha1(password.encode(encoding='utf-8')).hexdigest())
            user.password = hashlib.sha1(password.encode(encoding='utf-8')).hexdigest()
            try:
                user.save()
                request.session['uid'] = user.id
                return HttpResponseRedirect(nextpath)
            except Exception as e:
                print(e)
                return HttpResponseRedirect('/signup/',kargs={'nextpath':nextpath})

    return HttpResponseRedirect('/signup/',kargs={'nextpath':nextpath})

@csrf_exempt
def signup_comfirm(request):
    if request.method == 'POST':
        username = request.POST.get("username","")
        email = request.POST.get("email","")
        has_name = False
        has_email = False
        try:
            User.objects.get(name=username)
            has_name = True
        except Exception as e:
            pass
        try:
            User.objects.get(email=email)
            has_email = True
        except Exception as e:
            pass
        if has_name or has_email :
            msg_type = "error"
            msg = "用户名或邮箱已存在"
        else:
            msg_type = "success"
            msg = "用户名邮箱或未被注册"
        return HttpResponse(json.dumps({"msg_type":msg_type,"msg":msg}));
    return HttpResponse("");

def signin(request):
    nextpath = request.GET.get('next')
    return render(request,'omretuser/signin.html',{'nextpath':nextpath})

@csrf_protect
def signin_submit(request):
    nextpath = request.GET.get('next')
    if request.method == 'POST':
        username = request.POST.get("username","")
        password = request.POST.get("password","")
        if (username.strip() and password.strip()) != '' :
            try:
                user = User.objects.get(name=username)
                if user.password == hashlib.sha1(password.encode(encoding='utf-8')).hexdigest():
                    request.session['uid'] = user.id
                    return HttpResponseRedirect(nextpath)
                else:
                    return render(request,'omretuser/signin.html',{'msg':'用户名或密码错误','nextpath':nextpath})
            except Exception as e:
                return render(request,'omretuser/signin.html',{'msg':'用户名或密码错误','nextpath':nextpath})
    return HttpResponseRedirect('/signin/',kargs={'nextpath':nextpath})
