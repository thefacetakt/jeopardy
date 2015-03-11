from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    title = models.TextField()

class Question(models.Model):
    _100 = 100
    _200 = 200
    _300 = 300
    _400 = 400
    _500 = 500
    
    PRICES = (
        (_100, 100),
        (_200, 200),
        (_300, 300),
        (_400, 400),
        (_500, 500),
    )

    readingTime = models.FloatField()
    answeringTime = models.FloatField()
    price = models.IntegerField(choices=PRICES)
    statement = models.TextField()
    answer = models.TextField()
    category = models.ForeignKey(Category)
    author = models.ForeignKey(User)

class Result(models.Model):
    user = models.ForeignKey(User)
    score = models.IntegerField()

class Game(models.Model):
    results = models.ManyToManyField(Result)
    questions = models.ManyToManyField(Question)
    author = models.ForeignKey(User)


# Create your models here.
