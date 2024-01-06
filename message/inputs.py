import graphene

class KeyInput(graphene.InputObjectType):
    value = graphene.String()

class ChatboxInput(graphene.InputObjectType):
    owner = graphene.Int()
    users = graphene.List(graphene.Int)

class MessageInput(graphene.InputObjectType):
    owner = graphene.Int()
    chatbox = graphene.Int()
    value = graphene.String()
    users = graphene.List(graphene.Int)

class HashInput(graphene.InputObjectType):
    chatbox = graphene.Int()
    value = graphene.String()

class NotificationInput(graphene.InputObjectType):
    viewed = graphene.Boolean()
    value = graphene.String()
    chatbox = graphene.Int()
    owner = graphene.Int()
