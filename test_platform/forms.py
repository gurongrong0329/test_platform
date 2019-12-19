# -*- coding: utf-8 -*-
# 作者: 顾名思义
# 时间: 2019/12/17 21:20
# 文件: forms.py
from django import forms
from test_platform.models.project import Project

class ProjectForm(forms.ModelForm):

    class Meta:
        model=Project
        fields=['name','describe','status']