import graphene

class UserInput(graphene.InputObjectType):
    id = graphene.ID()
    username = graphene.String()
    email = graphene.String()
    admin = graphene.String()
    date_created = graphene.DateTime()
    date_update = graphene.DateTime()

class HashInput(graphene.InputObjectType):
    id = graphene.ID()
    user = graphene.String()
    value = graphene.String()
    date_created = graphene.DateTime()
    date_update = graphene.DateTime()

class KeyInput(graphene.InputObjectType):
    id = graphene.ID()
    value = graphene.String()
    date_created = graphene.DateTime()
    date_update = graphene.DateTime()
    