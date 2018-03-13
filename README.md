# BlogwithDjango

#环境：Win10+Django 1.8.3+ python 2.7.11

#创建项目与app
django-admin startproject mysite
cd testBlog #在项目下创建app
django-admin startapp blog

#在setting.py添加MyBlog应用
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
]

#数据库配置setting.py（若使用默认的sqlite3则不需修改）
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

#创建模型model.py
from __future__ import unicode_literals
from django.contrib import admin
from django.db import models
 
class BlogPost(models.Model):
 title = models.CharField(max_length=150)
 body = models.TextField()
 timestamp = models.DateTimeField()
 
 def __unicode__(self):
  return self.title

#Admin 管理(可添加在admin.py或model.py,添加在admin.py需要from MyBlog.models import BlogPost )
class BlogPostAdmin(admin.ModelAdmin):
 list_display = ('title','timestamp')
 
admin.site.register(BlogPost)

#创建模板
#在testBlog文件夹新建templates文件夹，然后添加index.html文件
#需要注意的就是模板中的模板标签以及模板变量都应该与views.py文件对应的函数中的字典变量相一致，否则django虽然不会报错，但也是不会显示数据的

#创建视图函数
from django.shortcuts import render
from blog.models import BlogPost


def myblogs(request):
    blog_list = BlogPost.objects.all()
    return render(request, 'index.html', {'blog_list':blog_list})

#创建MyBlog的URL模式
from django.conf.urls import url
from django.contrib import admin
from blog.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^Blog/$', myblogs),
]

#启动服务
python manage.py runserver

#上传博客
127.0.0.1:8000/admin
#要想登录admin后台，必须要有帐号，需要创建超级管理员帐号
python manage.py createsuperuser

#访问博客
127.0.0.1:8000/Blog

