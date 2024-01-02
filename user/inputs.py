import graphene

class UserInput(graphene.InputObjectType):
    id = graphene.Int()
    username = graphene.String()
    email = graphene.String()
    admin = graphene.String()
    date_created = graphene.DateTime()
    date_update = graphene.DateTime()

class HashInput(graphene.InputObjectType):
    id = graphene.Int()
    user = graphene.Int()
    value = graphene.String()
    date_created = graphene.DateTime()
    date_update = graphene.DateTime()

class KeyInput(graphene.InputObjectType):
    id = graphene.Int()
    value = graphene.String()
    date_created = graphene.DateTime()
    date_update = graphene.DateTime()
    