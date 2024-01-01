from graphene_django import DjangoObjectType
from django.contrib.auth.models import User
from .models import Hash, Key

class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = '__all__'


class HashType(DjangoObjectType):
    class Meta:
        model = Hash
        fields = '__all__'

class KeyType(DjangoObjectType):
    class Meta:
        model = Key
        fields = '__all__'