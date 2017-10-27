# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Article,Classify,Tag

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title','create_time','update_time','excerpt','auth','classifies']
admin.site.register(Article,ArticleAdmin)
admin.site.register(Classify)
admin.site.register(Tag)