"""
WEEK5_DJANGO URL Configuration

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

# Uncomment next two lines to enable admin:
from django.contrib import admin
from django.urls import path, include
from django.urls import re_path as url
from . import views

urlpatterns = [
    # Uncomment the next line to enable the admin:
    #path('admin/', admin.site.urls), -- first example and calender
    path(r'^admin/', admin.site.urls),
    # url(r'^$', views.index, name='index'),  # -- first example
    url(r'^(?P<year>[0-9]{4})/(?P<month>0?[1-9]|1[0-2])/', views.index, name='index'), # -- calender 
    url('^Form', include('formapp.urls')),  # add Form in url to get result
    url('^Q1', include('Q1.urls')),  # add Q1 in url to get result
    url('^Q2', include('Q2.urls')),
    # if do not mention Form and write '' then this will run regardless of whether we give year/month
]
