# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Article,Classify
from django.shortcuts import get_object_or_404
from comments.forms import CommentsForm
import markdown

from django.http import HttpResponse

# Create your views here.
#主页
def index(request):
    post_list = Article.objects.all().order_by('-create_time')
    return render(request,'blog/index.html',context={'post_list':post_list})
#文章详情
def detail(request,pk):
    post = get_object_or_404(Article,pk=pk)
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                     'markdown.extensions.extra',
                                     'markdown.extensions.codehilite',
                                     'markdown.extensions.toc',
                                  ])
    form = CommentsForm()
    comment_list = post.comments_set.all()
    context = {'post':post,
               'form':form,
               'comment_list':comment_list
               }

    return render(request,'blog/detail.html',context=context)
#归档
def archives(request,year,month):
    post_list = Article.objects.filter(update_time__year=year,
                                       update_time__month=month,
                                       ).order_by('-create_time')
    return render(request,'blog/index.html',context={'post_list':post_list})
#分类
def classifies(request,pk):
    cate = get_object_or_404(Classify,pk=pk)
    post_list = Article.objects.filter(classifies=cate).order_by('-create_time')
    return render(request,'blog/index.html',context={'post_list':post_list})

