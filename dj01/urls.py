"""dj01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from test_platform import views
from test_platform.views import login_view,module_view,project_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',login_view.login),
    path('login/',login_view.login),
    path('accounts/login/',login_view.login),
    path('project/',project_view.project_manage),
    path('add/',project_view.project_add),
    path('project/edit/<int:pid>/',project_view.project_edit),
    path('project/delete/<int:pid>/',project_view.project_delete),
    path('logout/',login_view.logout),
    path('module/',module_view.module_manage),
    path('/module/add/',module_view.module_add),
]
