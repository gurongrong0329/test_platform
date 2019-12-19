# -*- coding: utf-8 -*-
# 作者: 顾名思义
# 时间: 2019/12/17 21:20
# 文件: forms.py
from django import forms
from test_platform.models.project import Project
from test_platform.models.module import Module

class ProjectForm(forms.ModelForm):

    class Meta:
        model=Project
        fields=['name','describe','status']

class ModuleForm(forms.ModelForm):

    class Meta:
        model=Module
        fields=['name','describe','project']