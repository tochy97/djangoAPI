from email import message
from django.db import models
from django.contrib.auth.models import User


class Data(models.Model):
    id = models.IntegerField(primary_key=True)
    text = models.CharField(max_length=255)


class Quote(models.Model):
    id = models.IntegerField(primary_key=True)
    origin = models.CharField(max_length=50)
    text = models.CharField(max_length=255)

class Day(models.Model):
    id = models.IntegerField(primary_key=True)
    value = models.IntegerField()
    index = models.IntegerField()
    name = models.CharField(max_length=9)
    data = models.ForeignKey(Data, on_delete=models.CASCADE)


class Month(models.Model):
    id = models.IntegerField(primary_key=True)
    index = models.IntegerField()
    name = models.CharField(max_length=9)
    day = models.ForeignKey(Day, on_delete=models.CASCADE)


class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=255)
    content = models.CharField(max_length=10000)
