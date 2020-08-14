"""mybook URL Configuration

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
from django.urls import re_path

from app01 import views

urlpatterns = [
    # ------------------- 登录 -------------------
    re_path(r'^login/$', views.login),  # 登录

    # ------------------- 列表 -------------------
    re_path(r'^press_list/$', views.press_list),  # 出版社列表
    re_path(r'^book_list/$', views.book_list),  # 图书列表
    re_path(r'^author_list/$', views.author_list),  # 作者列表

    # ------------------- 添加 -------------------
    re_path(r'^add_author/$', views.add_author),
    re_path(r'^add_press/$', views.add_press),
    re_path(r'^add_book/$', views.add_book),

    # ------------------- 编辑 -------------------
    re_path(r'^edit_author/$', views.edit_author),
    re_path(r'^edit_press/$', views.edit_press),
    re_path(r'^edit_book/$', views.edit_book),

    # ------------------- 删除 -------------------
    re_path(r'^delete_press/$', views.delete_press),
    re_path(r'^delete_author/$', views.delete_author),
    re_path(r'^delete_book/$', views.delete_book),
]
