import graphene

class ScheduleInput(graphene.InputObjectType):
    id = graphene.Int()
    owner = graphene.Int()
    value = graphene.DateTime()
    description = graphene.String()

class HashInput(graphene.InputObjectType):
    id = graphene.Int()
    owner = graphene.Int()
    value = graphene.String()

class KeyInput(graphene.InputObjectType):
    id = graphene.Int()
    value = graphene.String()
    