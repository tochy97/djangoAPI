from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class AutoDateTimeField(models.DateTimeField):
    def pre_save(self, model_instance, add):
        return datetime.now()

class Schedule(models.Model):
    id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    value = models.DateTimeField()
    description = models.CharField(max_length=500, unique=True)
    date_created = models.DateTimeField(default=datetime.now)
    date_update = AutoDateTimeField(default=datetime.now)

    def __str__(self):
        return self.owner.username + '.' + str(self.id)

class Key(models.Model):
    id = models.AutoField(primary_key=True)
    value = models.CharField(max_length=129, unique=True)
    date_created = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.id

class Hash(models.Model):
    id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    value = models.CharField(max_length=129, unique=True)
    date_created = models.DateTimeField(default=datetime.now)
    date_update = AutoDateTimeField(default=datetime.now)

    def __str__(self):
        return self.owner.username + '.' + str(self.id)
