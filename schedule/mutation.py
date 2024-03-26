from graphene import ObjectType, Mutation, Field, String, Boolean, ID
from django.contrib.auth.models import User
from datetime import datetime
from graphql_auth import mutations
import graphql_jwt

from .models import Schedule, Key, Hash
from .types import ScheduleType, KeyType, HashType
from .inputs import ScheduleInput, KeyInput, HashInput

class CreateSchedule(Mutation):

    class Arguments:
        schedule_input = ScheduleInput(required=True)

    schedule = Field(ScheduleType)
        
    @classmethod
    def mutate(cls, root, info, schedule_input):
        now = datetime.now()
        schedule=Schedule(
            owner = User.objects.get(pk=schedule_input.owner),
            value = schedule_input.value,
            description = schedule_input.description,
        )
        schedule.save()
        return CreateSchedule(schedule=schedule)
    
class UpdateSchedule(Mutation):
    
    class Arguments:
        schedule_input = ScheduleInput(required=True)

    schedule = Field(ScheduleType)
        
    @classmethod
    def mutate(cls, root, info, schedule_input):
        auth = info.context.user
        if not auth.is_authenticated:
            raise Exception("Authentication credentials were not provided")
        schedule = Schedule.objects.get(pk=schedule_input.id)
        schedule.value = schedule_input.value
        schedule.description = schedule_input.description
        schedule.save()
        return UpdateSchedule(schedule=schedule)
    
class DeleteSchedule(Mutation):
    
    class Arguments:
        schedule_input = ScheduleInput(required=True)

    schedule = Field(ScheduleType)

    @classmethod
    def mutate(cls, root, info, schedule_input):
        auth = info.context.user
        if not auth.is_authenticated:
            raise Exception("Authentication credentials were not provided")
        schedule = Schedule.objects.get(pk=schedule_input.id)
        schedule.delete()
        return None
    
class CreateKey(Mutation):
    
    class Arguments:
        key_input = KeyInput(required=True)

    key = Field(KeyType)
        
    @classmethod
    def mutate(cls, root, info, key_input):
        key = Key(
            value = key_input.value
        )
        key.save()
        return CreateKey(key=key)
    
class UpdateKey(Mutation):
    
    class Arguments:
        key_input = KeyInput(required=True)

    key = Field(KeyType)
        
    @classmethod
    def mutate(cls, root, info, key_input):
        key = Key.objects.get(pk=key_input.id)
        key.value = key_input.value
        key.save()
        return UpdateKey(key=key)
    
class CreateHash(Mutation):

    class Arguments:
        hash_input = HashInput(required=True)

    hash = Field(HashType)
        
    @classmethod
    def mutate(cls, root, info, hash_input):
        now = datetime.now()
        hash=Hash(
            owner = User.objects.get(pk=hash_input.owner),
            value = hash_input.value,
        )
        hash.save()
        return CreateHash(hash=hash)
    
class UpdateHash(Mutation):
    
    class Arguments:
        hash_input = HashInput(required=True)

    hash = Field(HashType)
        
    @classmethod
    def mutate(cls, root, info, hash_input):
        auth = info.context.user
        if not auth.is_authenticated:
            raise Exception("Authentication credentials were not provided")
        hash = Hash.objects.get(pk=hash_input.id)
        hash.value = hash_input.value
        hash.save()
        return UpdateHash(hash=hash)
    
class DeleteHash(Mutation):
    
    class Arguments:
        hash_input = HashInput(required=True)

    hash = Field(HashType)
        
    @classmethod
    def mutate(cls, root, info, hash_input):
        auth = info.context.user
        if not auth.is_authenticated:
            raise Exception("Authentication credentials were not provided")
        hash = Hash.objects.get(pk=hash_input.id)
        hash.delete()
        return None
    
class Mutation(ObjectType):
    create_key = CreateKey.Field()
    update_key = UpdateKey.Field()
    
    create_hash = CreateHash.Field()
    update_hash = UpdateHash.Field()
    delete_hash = DeleteHash.Field()
