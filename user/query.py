from graphene import List, ObjectType
from django.contrib.auth.models import User

from .models import Setting, Key, Hash
from .types import UserType, KeyType, HashType
        
class Query(ObjectType):
    all_Hash = List(HashType)
    def resolve_all_Hash(root, info):
        return Hash.objects.all()
    
    all_Key = List(HashType)

    all_User = List(UserType)
    def resolve_all_user(root, info):
        return User.objects.all()
    