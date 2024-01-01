from graphene import ObjectType, Schema

import user.schema
import user.hash

class Query(
    user.schema.Query, 
    ObjectType
):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass

class Mutation(
    user.schema.Mutation,
    ObjectType
):
    pass

schema = Schema(query=Query, mutation=Mutation)