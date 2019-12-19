# -*- coding: utf-8 -*-
# 作者: 顾名思义
# 时间: 2019/12/16 20:21
# 文件: module_view.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from test_platform.models.module import Module

@login_required
def module_manage(request):
    module_all=Module.objects.all()
    return render(request,'module.html',{'type':'list','module_all':module_all})

@login_required
def module_add(request):
    module_all=Module.objects.all()
    return render(request,'module.html',{'type':'list','module_all':module_all})