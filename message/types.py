from graphene_django import DjangoObjectType
from django.contrib.auth.models import User

from .models import Key, Chatbox, Message, Hash, Notification

class KeyType(DjangoObjectType):
    class Meta:
        model = Key
        fields = '__all__'

class ChatboxType(DjangoObjectType):
    class Meta:
        model = Chatbox
        fields = '__all__'

class MessageType(DjangoObjectType):
    class Meta:
        model = Message
        fields = '__all__'

class HashType(DjangoObjectType):
    class Meta:
        model = Hash
        fields = '__all__'

class NotificationType(DjangoObjectType):
    class Meta:
        model = Notification
        fields = '__all__'
        
class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = '__all__'