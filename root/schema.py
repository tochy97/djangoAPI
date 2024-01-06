from graphene import ObjectType, Schema

import user.schema
import message.schema

class Query(
    user.schema.Query, 
    message.schema.Query, 
    ObjectType
):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass

class Mutation(
    user.schema.Mutation,
    message.schema.Mutation,
    ObjectType
):
    pass

schema = Schema(query=Query, mutation=Mutation)