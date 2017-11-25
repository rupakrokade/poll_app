# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.db import models
# Register your models here.

from blog.models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ['title','body']
    list_filter = ['date']


admin.site.register(Post, PostAdmin)
