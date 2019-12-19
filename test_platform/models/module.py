# -*- coding: utf-8 -*-
# 作者: 顾名思义
# 时间: 2019/12/5 20:03
# 文件: module.py
from django.db import models
from test_platform.models.project import Project

# Create your models here.

class Module(models.Model):
    name = models.CharField('名称',max_length=10, null=False)
    describe = models.TextField('描述',default="")
    create_time = models.DateTimeField('创建时间',auto_now=True)
    project = models.ForeignKey(Project,on_delete=models.CASCADE)

    def __str__(self):
        return self.name