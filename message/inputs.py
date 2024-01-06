import graphene

class KeyInput(graphene.InputObjectType):
    id = graphene.Int()
    value = graphene.String()
    date_created = graphene.DateTime()
    date_update = graphene.DateTime()

class ChatboxInput(graphene.InputObjectType):
    id = graphene.Int()
    owner = graphene.Int()
    users = graphene.List(graphene.Int)
    date_created = graphene.DateTime()
    date_update = graphene.DateTime()

class MessageInput(graphene.InputObjectType):
    id = graphene.Int()
    owner = graphene.Int()
    chatbox = graphene.Int()
    value = graphene.String()
    date_created = graphene.DateTime()

class HashInput(graphene.InputObjectType):
    id = graphene.Int()
    chatbox = graphene.Int()
    value = graphene.String()
    date_created = graphene.DateTime()
    date_update = graphene.DateTime()

class NotificationInput(graphene.InputObjectType):
    id = graphene.Int()
    owner = graphene.Int()
