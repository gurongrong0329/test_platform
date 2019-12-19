# -*- coding: utf-8 -*-
# 作者: 顾名思义
# 时间: 2019/12/16 20:21
# 文件: project_view.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from test_platform.models.project import Project
from django.http import HttpResponse,HttpResponseRedirect
from test_platform.forms import ProjectForm

@login_required
def project_manage(request):
    project_all=Project.objects.all()
    return render(request,'project.html',{'type':'list','project_all':project_all})

@login_required
def project_add(request):
    if request.method == 'GET':
        return render(request,'project.html',{'type':'add'})
    elif request.method == 'POST':
        name=request.POST.get('name','')
        describe=request.POST.get('describe','')
        status=request.POST.get('status','')
        if name == '':
            return render(request,'project.html',{'type':'add','name_error':'名称不能为空'})
        Project.objects.create(name=name,describe=describe,status=status)
        return HttpResponseRedirect('/project/')

@login_required
def project_edit(request,pid):
    if request.method == 'GET':
       data=Project.objects.get(id=pid)
       form=ProjectForm(instance=data)
       return render(request, 'project.html', {'type': 'edit','form':form,'pid':pid})

    elif request.method == 'POST':
       form = ProjectForm(request.POST)
       if form.is_valid():
           name = form.cleaned_data['name']
           describe = form.cleaned_data['describe']
           status = form.cleaned_data['status']
           p = Project.objects.get(id=pid)
           p.name = name
           p.describe = describe
           p.status = status
           p.save()
           return HttpResponseRedirect('/project/')

@login_required
def project_delete(request,pid):
    if request.method == 'GET':
        try:
            data=Project.objects.get(id=pid)
        except Project.DoesNotExist:
            return HttpResponseRedirect('/project/')
        else:
            data.delete()
        return HttpResponseRedirect('/project/')