from django.db import models

    
class Setting(models.Model):
    ID = models.CharField(primary_key=True, max_length=129)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=1)
    value = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Key(models.Model):
    ID = models.CharField(primary_key=True, max_length=129)
    value = models.CharField(max_length=129)
    date_created = models.DateTimeField()

    def __str__(self):
        return self.date_created

class Hash(models.Model):
    ID = models.CharField(primary_key=True, max_length=129)
    user = models.CharField(max_length=100)
    value = models.CharField(max_length=129)
    date_created = models.DateTimeField()
    date_update = models.DateTimeField()

    def __str__(self):
        return self.user


