from django.db import models

# Create your models here.

class Project(models.Model):
    name=models.CharField(max_length=10)
    describe=models.TextField(default="")
    status=models.BooleanField(default=1)
    create_time=models.DateTimeField(auto_now=True)


class Module(models.Model):
    name = models.CharField(max_length=10,null=False)
    describe = models.TextField(default="")
    status = models.BooleanField(default=1)
    create_time = models.DateTimeField(auto_now=True)
    project=models.ForeignKey(Project)