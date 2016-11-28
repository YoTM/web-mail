#!/usr/bin/env python
import uuid

from django.contrib.auth.models import User
from django.db import models

class QuestionManager(models.Manager):

        def new(self):
            qs = super(QuestionManager, self).get_queryset()
            return qs.order_by('-id')
        def popular(self):
            qs = super(QuestionManager, self).get_queryset()
            return qs.order_by('-rating')

class Question(models.Model):
    objects = QuestionManager()
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, related_name='question_author')
    likes = models.ManyToManyField(User, related_name='question_like')

    def get_url(selfself):
        return "/question/{}/".format(self.id)

    def __unicode__(self):
        return self.title

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateField(auto_now_add=True)
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User)

    def __unicode__(self):
        return self.title



