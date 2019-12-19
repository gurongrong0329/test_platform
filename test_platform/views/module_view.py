# -*- coding: utf-8 -*-
# 作者: 顾名思义
# 时间: 2019/12/16 20:21
# 文件: module_view.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from test_platform.models.module import Module
from django.http import HttpResponse,HttpResponseRedirect
from test_platform.forms import ModuleForm

@login_required
def module_manage(request):
    module_all=Module.objects.all()
    return render(request,'module.html',{'type':'list','module_all':module_all})

@login_required
def module_add(request):
    if request.method == 'GET':
        form=ModuleForm()
        return render(request,'module.html',{'type':'add','form':form})
    elif request.method == 'POST':
        form = ModuleForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            describe = form.cleaned_data['describe']
            project = form.cleaned_data['project']
            Module.objects.create(name=name,describe=describe,project=project)
        return HttpResponseRedirect('/module/')

@login_required
def module_edit(request,mid):
    if request.method == 'GET':
       data=Module.objects.get(id=mid)
       form=ModuleForm(instance=data)
       return render(request, 'module.html', {'type': 'edit','form':form,'mid':mid})

    elif request.method == 'POST':
       form = ModuleForm(request.POST)
       if form.is_valid():
           name = form.cleaned_data['name']
           describe = form.cleaned_data['describe']
           project = form.cleaned_data['project']
           m = Module.objects.get(id=mid)
           m.name = name
           m.describe = describe
           m.project = project
           m.save()
           return HttpResponseRedirect('/module/')

@login_required
def module_delete(request,mid):
    if request.method == 'GET':
        try:
            data=Module.objects.get(id=mid)
        except Module.DoesNotExist:
            return HttpResponseRedirect('/module/')
        else:
            data.delete()
        return HttpResponseRedirect('/module/')