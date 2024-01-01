from django.db import models
from django.contrib.auth.models import User

    
class Setting(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=1)
    value = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Key(models.Model):
    id = models.AutoField(primary_key=True)
    value = models.CharField(max_length=129)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.date_created

class Hash(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    value = models.CharField(max_length=129)
    date_created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField()

    def __str__(self):
        return self.user.username


