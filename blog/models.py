# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import resolve_url
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.

@python_2_unicode_compatible
#파이썬2랑 파이썬3이랑 다른 코드 둘다 사용 가능
class Post(models.Model):
    title = models.CharField(max_length=100,verbose_name='제목')
    content = models.TextField()
    photo = models.ImageField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return resolve_url('blog:post_detail',self.pk)

    def title_length(self):
        return len(self.title)


