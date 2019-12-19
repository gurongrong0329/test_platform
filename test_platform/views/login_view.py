# -*- coding: utf-8 -*-
# 作者: 顾名思义
# 时间: 2019/12/16 20:21
# 文件: login_view.py
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth

def login(request):
    """
    登录的首页
    :param request:
    :return:
    """
    if request.method=='GET':
        return render(request,'login.html')
    else:
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        print(username,password)
        if username == '' or password == '':
            return render(request, 'login.html', {'error': '用户名或密码错误'})
        user = auth.authenticate(username=username,password=password)
        print(user)
        if user is not None:
            auth.login(request,user)
            return HttpResponseRedirect('/project/')
        else:
            return render(request, 'login.html', {'error': '用户名或密码错误'})

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/project/')