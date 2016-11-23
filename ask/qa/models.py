from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Question(models, Model):
    objects = QuestionManager()
    title = models.CharField(max_lenght=255)
    text = models.TextField()
    added_at = models.DateField()
    rating = models.IntegerField()
    author = models.ForignKey(User)
    likes = models.ManyToManyField(User)

    class QuestionManager(models.Manager):
        def new(self):
                pass
        def popular(self):
                pass
class Answer(models, Model):
    text = models.TextField()
    added_at = models.DateField()
    question= models.ForignKey(Question)
    author = models.ForignKey(User)



