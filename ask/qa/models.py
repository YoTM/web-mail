#!/usr/bin/env python
from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class QuestionManager(models.Manager):
        def new(self):
                pass
        def popular(self):
                pass

class Question(models.Model):
    objects = QuestionManager()
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, default='x', related_name='question_author')
    likes = models.ManyToManyField(User, related_name='question_like')

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateField(auto_now_add=True)
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User)



