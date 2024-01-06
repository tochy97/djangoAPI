from django.contrib import admin
from .models import Chatbox, Message, Hash, Key
from django.apps import apps
# Register your models here.

admin.site.register(Chatbox)
admin.site.register(Message)
admin.site.register(Hash)
admin.site.register(Key)
