# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=300, verbose_name='تیتر پست')
    content = models.TextField(verbose_name='متن پست')
    create_date = models.DateTimeField()
    author_id = models.ForeignKey(User)

    def __str__(self):
        return self.title
