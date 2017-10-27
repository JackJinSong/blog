# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class Classify(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Article(models.Model):

    title = models.CharField('标题',max_length=100)
    body = models.TextField('正文')
    create_time = models.DateTimeField('创建时间',auto_now_add=True)
    update_time = models.DateTimeField('更新时间',auto_now=True)
    brief = models.CharField('摘要',max_length=200,blank=True)
    classifies= models.ForeignKey(Classify)
    tags = models.ManyToManyField(Tag,blank=True)
    auth = models.ForeignKey(User)
    point_good = models.IntegerField(default=0)
    view_count = models.IntegerField(default=0)
    views = models.PositiveIntegerField(default=0)

    def get_absolute_url(self):
        return reverse('news:detail',kwargs={'pk':self.pk})
    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])


    def __str__(self):
        return self.title
