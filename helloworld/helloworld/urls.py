"""helloworld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
# from django.contrib import admin
# from django.urls import path
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]

from django.conf.urls import url
from django.urls import re_path, path
from . import view
from hello import views

urlpatterns = [
    url(r'^$', view.index),
    url('^xy', view.xy),
    # url('^demo', views.demo),
    path("index/", views.index),
    re_path('^$', views.index),
    url('^demo/$', views.demo),
    url('^demo/page=(\d+)$', views.page),
    # 匹配archive/018/10.htm
    path("archive/<year>/<month>.html", views.home1),
    url(r'^archive1/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2}).html$', views.home1)
]

# url函数
"""
url() 可以接收四个参数，分别是两个必选参数：regex、view 和两个可选参数：kwargs、name.
def url(regex, view, kwargs=None, name=None):
    return re_path(regex, view, kwargs, name)
regex: 正则表达式，与之匹配的 URL 会执行对应的第二个参数 view。

view: 用于执行与正则表达式匹配的 URL 请求。

kwargs: 视图使用的字典类型的参数。

name: 用来反向获取 URL
"""
