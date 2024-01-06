from django.contrib import admin
from django.apps import apps

from .models import Chatbox, Message, Hash, Key, Notification
# Register your models here.

admin.site.register(Chatbox)
admin.site.register(Message)
admin.site.register(Hash)
admin.site.register(Key)
admin.site.register(Notification)
