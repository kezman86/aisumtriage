"""aisumtriage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

from webapp import views
import api.views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.index, name='index'),

    # Auth
    path ( 'signup/' , views.signupuser , name = 'signupuser' ) ,
    path ( 'login/' , views.loginuser , name = 'loginuser' ) ,
    path ( 'logout/' , views.logoutuser , name = 'logoutuser' ) ,


    #app
    path ( 'cases/' , views.cases , name = 'cases' ) ,
    path('completedcases/', views.completedcases, name='completedcases'),
    path('case/<caseID>/complete' , views.completecase, name='completecase'),
    path('case/<caseID>', views.viewcase , name='viewcase'),


    #api
    path('api/login' , api.views.loginapi, name='loginapi'),
    path('api/sampleapi', api.views.sample_api, name='sampleapi'),
    path('api/getAllCases', api.views.getAllCases , name='getAllCases'),
    path('api/approvecase', api.views.approvecase , name='approvecase')
]
