from graphene import List, ObjectType, Field, Int 
from django.contrib.auth.models import User

from .models import Setting, Key, Hash
from .types import UserType, KeyType, HashType
        
class Query(ObjectType):
    get_Hash = Field(HashType, id=Int())
    def resolve_get_Hash(root, info, id):
        return Hash.objects.get(pk=id)

    get_Key = Field(KeyType, id=Int())
    def resolve_get_Key(root, info, id):
        return Key.objects.get(pk=id)
    
    get_User = Field(UserType, id=Int())
    def resolve_get_User(root, info, id):
        return User.objects.get(pk=id)
    