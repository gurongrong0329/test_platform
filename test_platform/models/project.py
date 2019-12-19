# -*- coding: utf-8 -*-
# 作者: 顾名思义
# 时间: 2019/12/5 20:04
# 文件: project.py
from django.db import models

# Create your models here.

class Project(models.Model):
    name=models.CharField('名称',max_length=10)
    describe=models.TextField('描述',default="")
    status=models.BooleanField('状态',default=1)
    create_time=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name