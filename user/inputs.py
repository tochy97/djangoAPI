import graphene

class UserInput(graphene.InputObjectType):
    id = graphene.Int()
    username = graphene.String()
    email = graphene.String()
    admin = graphene.String()

class HashInput(graphene.InputObjectType):
    id = graphene.Int()
    owner = graphene.Int()
    value = graphene.String()

class KeyInput(graphene.InputObjectType):
    id = graphene.Int()
    value = graphene.String()
    