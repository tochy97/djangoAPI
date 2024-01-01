from graphene import Schema, ObjectType, Mutation

from .mutation import SaveHash, SaveKey, SaveUser
from .query import Query    

class Mutation(ObjectType):
    save_hash = SaveHash.Field()
    save_key = SaveKey.Field()
    save_user = SaveUser.Field()

schema = Schema(query=Query, mutation=Mutation)