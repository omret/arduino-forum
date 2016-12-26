from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect,csrf_exempt

import json
import hashlib

from .models import User

# Create your views here.
def signup(request):
    return render(request,'omretuser/signup.html',{})

@csrf_protect
def signup_submit(request):
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
                return HttpResponseRedirect('/')
            except Exception as e:
                print(e)
                return HttpResponseRedirect('/signup/')

    return HttpResponseRedirect('/signup/')

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
    return render(request,'omretuser/signin.html',{})

@csrf_protect
def signin_submit(request):
    if request.method == 'POST':
        username = request.POST.get("username","")
        password = request.POST.get("password","")
        if (username.strip() and password.strip()) != '' :
            try:
                user = User.objects.get(name=username)
                if user.password == hashlib.sha1(password.encode(encoding='utf-8')).hexdigest():
                    return HttpResponseRedirect('/')
                else:
                    return render(request,'omretuser/signin.html',{'msg':'用户名或密码错误'})
            except Exception as e:
                return render(request,'omretuser/signin.html',{'msg':'用户名或密码错误'})
    return HttpResponseRedirect('/signin/')
