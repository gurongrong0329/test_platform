from django.contrib import admin
from test_platform.models.project import Project
from test_platform.models.module import Module
# Register your models here.
"""
django管理后台
"""
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id','name','status','describe','create_time']
    search_fields = ['name']

class ModuleAdmin(admin.ModelAdmin):
    list_display = ['id','name','status','describe','create_time','project']
    search_fields = ['name']


admin.site.register(Project,ProjectAdmin)
admin.site.register(Module,ModuleAdmin)