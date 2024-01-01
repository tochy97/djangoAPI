from graphene import Mutation, Field, String, Boolean, ID
from django.contrib.auth.models import User

from .models import Setting, Key, Hash
from .types import UserType, KeyType, HashType
from .inputs import UserInput, KeyInput, HashInput

class SaveUser(Mutation):
    user = Field(UserType)
    #input arguments
    class Arguments:
        user_input = UserInput()
        
    def mutate(self, info, user_input=None):
        user=User(
            id = user_input.id,
            username = user_input.username,
            email = user_input.email,
            admin = user_input.admin,
            date_created = user_input.date_created,
        )
        user.save()
        ok = True
        return SaveUser(user=user)

class SaveKey(Mutation):
    key = Field(KeyType)
    #input arguments
    class Arguments:
        key_input = KeyInput(required=True)
        
    def mutate(self, info, key_input=None):
        key=Key(
            user = key_input.user,
            value = key_input.value,
            date_created = key_input.date_created,
        )
        key.save()
        ok = True
        return SaveHash(key=key)

class SaveHash(Mutation):
    hash = Field(HashType)
    #input arguments
    class Arguments:
        hash_input = HashInput(required=True)
        
    def mutate(self, info, hash_input=None):
        hash=Hash(
            user = hash_input.user,
            value = hash_input.value,
            date_created = hash_input.date_created,
        )
        hash.save()
        ok = True
        return SaveHash(hash=hash)