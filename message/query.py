from graphene import ObjectType, Field, Int, List
from graphql_auth.schema import UserQuery, MeQuery 
from django.contrib.auth.models import User

from .models import Key, Hash, Chatbox, Message, Notification
from .types import UserType, KeyType, HashType, ChatboxType, MessageType, NotificationType
        
class Query(UserQuery, MeQuery, ObjectType):
    get_chatboxHash = Field(HashType, id=Int())
    def resolve_get_Hash(root, info, id):
        return Hash.objects.get(pk=id)

    get_messageKey = Field(KeyType, id=Int())
    def resolve_get_Key(root, info, id):
        return Key.objects.get(pk=id)
    
    get_AllUserChat = List(ChatboxType, owner=Int())
    def resolve_get_AllUserChat(root, info, owner):
        if owner:
            return Chatbox.objects.filter(owner=owner)

    get_Chat = Field(ChatboxType, id=Int())
    def resolve_get_Chatbox(root, info, id):
        return Chatbox.objects.get(pk=id)
    
    get_Message = Field(MessageType, id=Int())
    def resolve_get_Message(root, info, id):
        return Message.objects.get(pk=id)
    
    get_Notification = Field(NotificationType, id=Int())
    def resolve_get_Notification(root, info, id):
        return Notification.objects.get(pk=id)