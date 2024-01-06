from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class AutoDateTimeField(models.DateTimeField):
    def pre_save(self, model_instance, add):
        return datetime.now()

class Key(models.Model):
    id = models.AutoField(primary_key=True)
    value = models.CharField(max_length=129, unique=True)
    date_created = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.id
    
class Chatbox(models.Model):
    id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(User, default=1, on_delete=models.CASCADE, related_name = "owner")
    users = models.ManyToManyField(User)
    date_created = models.DateTimeField(default=datetime.now)
    date_update = AutoDateTimeField(default=datetime.now)

    def __str__(self):
        return self.owner.username + '.' + str(self.id)

class Message(models.Model):
    id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    chatbox = models.ForeignKey(Chatbox, default=1, on_delete=models.CASCADE)
    value = models.TextField(null=True)
    date_created = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.owner.username + '.' + str(self.chatbox.id) + '.' + str(self.id)
    
class Hash(models.Model):
    id = models.AutoField(primary_key=True)
    chatbox = models.ForeignKey(Chatbox, default=1, on_delete=models.CASCADE)
    value = models.CharField(max_length=129, unique=True)
    date_created = models.DateTimeField(default=datetime.now)
    date_update = AutoDateTimeField(default=datetime.now)

    def __str__(self):
        return self.chatbox.owner.username + '.' + str(self.chatbox.id) + '.' + str(self.id)
    
class Notification(models.Model):
    id = models.AutoField(primary_key=True)
    viewed = models.BooleanField(default=False)
    value = models.TextField(null=True)
    chatbox = models.ForeignKey(Chatbox, default=1, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, default=1, on_delete=models.CASCADE)

    def __str__(self):
        return self.owner.username + '.' + str(self.id)
    