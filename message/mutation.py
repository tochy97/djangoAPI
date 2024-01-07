from graphene import ObjectType, Mutation, Field, String, Boolean, ID
from django.contrib.auth.models import User
from datetime import datetime
from graphql_auth import mutations
import graphql_jwt

from .models import Key, Hash, Message, Chatbox, Notification
from .types import KeyType, HashType, ChatboxType, MessageType, NotificationType
from .inputs import KeyInput, HashInput, MessageInput, ChatboxInput, NotificationInput

# *** Key *** #
class CreateKey(Mutation):
    
    class Arguments:
        key_input = KeyInput(required=True)

    key = Field(KeyType)
        
    @classmethod
    def mutate(cls, root, info, key_input):
        key = Key(
            value = key_input.value
        )
        key.save()
        return CreateKey(key=key)
    
class UpdateKey(Mutation):
    
    class Arguments:
        key_input = KeyInput(required=True)

    key = Field(KeyType)
        
    @classmethod
    def mutate(cls, root, info, key_input):
        key = Key.objects.get(pk=key_input.id)
        key.value = key_input.value
        key.save()
        return UpdateKey(key=key)

# *** Hash *** #
class CreateHash(Mutation):

    class Arguments:
        hash_input = HashInput(required=True)

    hash = Field(HashType)
        
    @classmethod
    def mutate(cls, root, info, hash_input):
        now = datetime.now()
        hash=Hash(
            chatbox = User.objects.get(pk=hash_input.chatbox),
            value = hash_input.value,
        )
        hash.save()
        return CreateHash(hash=hash)
    
class UpdateHash(Mutation):
    
    class Arguments:
        hash_input = HashInput(required=True)

    hash = Field(HashType)
        
    @classmethod
    def mutate(cls, root, info, hash_input):
        auth = info.context.user
        if not auth.is_authenticated:
            raise Exception("Authentication credentials were not provided")
        hash = Hash.objects.get(pk=hash_input.id)
        hash.value = hash_input.value
        hash.save()
        return UpdateHash(hash=hash)
    
class DeleteHash(Mutation):
    
    class Arguments:
        hash_input = HashInput(required=True)

    hash = Field(HashType)
        
    @classmethod
    def mutate(cls, root, info, hash_input):
        auth = info.context.user
        if not auth.is_authenticated:
            raise Exception("Authentication credentials were not provided")
        hash = Hash.objects.get(pk=hash_input.id)
        hash.delete()
        return None

# *** Notification *** #
class CreateNotification(Mutation):

    class Arguments:
        notification_input = NotificationInput(required=True)

    notification = Field(NotificationType)
        
    @classmethod
    def mutate(cls, root, info, notification_input):
        now = datetime.now()
        notification=Notification(
            owner = User.objects.get(pk=notification_input.owner),
            chatbox = Chatbox.objects.get(pk=notification_input.chatbox),
            viewed = notification_input.viewed,
            value = notification_input.value,
        )
        notification.save()
        return CreateNotification(notification=notification)
    
class UpdateNotification(Mutation):
    
    class Arguments:
        notification_input = NotificationInput(required=True)

    notification = Field(NotificationType)
        
    @classmethod
    def mutate(cls, root, info, notification_input):
        auth = info.context.user
        if not auth.is_authenticated:
            raise Exception("Authentication credentials were not provided")
        notification = Notification.objects.get(pk=notification_input.id)
        notification.viewed = notification_input.viewed
        notification.save()
        return UpdateNotification(notification=notification)
    
class DeleteNotification(Mutation):
    
    class Arguments:
        notification_input = NotificationInput(required=True)

    notification = Field(NotificationType)
        
    @classmethod
    def mutate(cls, root, info, notification_input):
        auth = info.context.user
        if not auth.is_authenticated:
            raise Exception("Authentication credentials were not provided")
        notification = Notification.objects.get(pk=notification_input.id)
        notification.delete()
        return None
    
# *** Message *** #
class CreateMessage(Mutation):

    class Arguments:
        message_input = MessageInput(required=True)

    message = Field(MessageType)
        
    @classmethod
    def mutate(cls, root, info, message_input):
        auth = info.context.user
        if not auth.is_authenticated:
            raise Exception("Authentication credentials were not provided")
        now = datetime.now()
        chatbox = Chatbox.objects.get(pk=message_input.chatbox)
        owner = User.objects.get(pk=message_input.owner)
        message=Message(
            owner = User.objects.get(pk=message_input.owner),
            chatbox = Chatbox.objects.get(pk=message_input.chatbox),
            count = message_input.count,
            value = message_input.value,
        )

        # Create notification
        for user in message_input.users:
            reciever = User.objects.get(pk=user)
            notificatoin = Notification(
                owner = reciever,
                value = "New message from: " + owner.username,
                chatbox = chatbox
            )
            notificatoin.save()

        message.save()
        return CreateMessage(message=message)
    
class UpdateMessage(Mutation):
    
    class Arguments:
        message_input = MessageInput(required=True)

    message = Field(MessageType)
        
    @classmethod
    def mutate(cls, root, info, message_input):
        auth = info.context.user
        if not auth.is_authenticated:
            raise Exception("Authentication credentials were not provided")
        message = Message.objects.get(pk=message_input.id)
        message.value = message_input.value
        message.save()
        return UpdateMessage(message=message)
    
class DeleteMessage(Mutation):
    
    class Arguments:
        message_input = MessageInput(required=True)

    message = Field(MessageType)
        
    @classmethod
    def mutate(cls, root, info, message_input):
        auth = info.context.user
        if not auth.is_authenticated:
            raise Exception("Authentication credentials were not provided")
        message = Message.objects.get(pk=message_input.id)
        message.delete()
        return None

# *** Chatbox *** #
class CreateChatbox(Mutation):

    class Arguments:
        chatbox_input = ChatboxInput(required=True)

    chatbox = Field(ChatboxType)
        
    @classmethod
    def mutate(cls, root, info, chatbox_input):
        auth = info.context.user
        if not auth.is_authenticated:
            raise Exception("Authentication credentials were not provided")
        now = datetime.now()
        owner = User.objects.get(pk=chatbox_input.owner)

        chatbox=Chatbox(
            owner = owner,
        )
        chatbox.save()

        # Add users
        for user in chatbox_input.users:
            addMe = User.objects.get(pk=user)
            chatbox.users.add(addMe.id)

        # Create notification
        for user in chatbox_input.users:
            reciever = User.objects.get(pk=user)
            notificatoin = Notification(
                owner = reciever,
                value = "New chat from: " + owner.username,
                chatbox = chatbox
            )
            notificatoin.save()

        return CreateChatbox(chatbox=chatbox)
    
class UpdateChatbox(Mutation):
    
    class Arguments:
        chatbox_input = ChatboxInput(required=True)

    chatbox = Field(ChatboxType)
        
    @classmethod
    def mutate(cls, root, info, chatbox_input):
        auth = info.context.user
        if not auth.is_authenticated:
            raise Exception("Authentication credentials were not provided")
        users = []
        for user in chatbox_input.users:
            users.append(user)
        chatbox = Chatbox.objects.get(pk=chatbox_input.id)
        chatbox.users = chatbox_input.users
        chatbox.save()
        return UpdateChatbox(chatbox=chatbox)
    
class DeleteChatbox(Mutation):
    
    class Arguments:
        chatbox_input = ChatboxInput(required=True)

    chatbox = Field(ChatboxType)
        
    @classmethod
    def mutate(cls, root, info, chatbox_input):
        auth = info.context.user
        if not auth.is_authenticated:
            raise Exception("Authentication credentials were not provided")
        chatbox = Chatbox.objects.get(pk=chatbox_input.id)
        chatbox.delete()
        return None
    
class Mutation(ObjectType):
    create_messageKey = CreateKey.Field()
    update_messagekey = UpdateKey.Field()

    create_chatboxHash = CreateHash.Field()
    update_chatboxHash = UpdateHash.Field()
    delete_chatboxHash = DeleteHash.Field()

    create_message = CreateMessage.Field()
    update_message = UpdateMessage.Field()
    delete_message = DeleteMessage.Field()

    create_chatbox = CreateChatbox.Field()
    update_chatbox = UpdateChatbox.Field()
    delete_chatbox = DeleteChatbox.Field()

    create_chatboxNotification = CreateNotification.Field()
    update_chatboxNotification = UpdateNotification.Field()
    delete_chatboxNotification = DeleteNotification.Field()