from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Document(models.Model):
    id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(User, default=1, on_delete=models.CASCADE, related_name = "owner")
    name = models.TextField(null=True)
    date_created = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.owner.username + '.' + str(self.id)
