# -*- coding: utf-8 -*-
# 作者: 顾名思义
# 时间: 2019/12/17 21:20
# 文件: forms.py
from django import forms
from test_platform.models.project import Project

class ProjectForm(forms.ModelForm):
    # name=forms.CharField(label='名称',max_length=10)
    # describe=forms.CharField(label='描述',widget=forms.Textarea,max_length=100)
    # status=forms.BooleanField(label='状态',required=True)

    class Meta:
        model=Project
        fields=['name','describe','status']