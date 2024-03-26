from graphene import ObjectType, Mutation, Field, String, Boolean, ID
from django.contrib.auth.models import User
from datetime import datetime
from graphql_auth import mutations
import graphql_jwt

from .models import Document
from .types import DocumentType
from .inputs import DocumentInput

# *** document *** #
class CreateDocument(Mutation):
    
    class Arguments:
        document_input = DocumentInput(required=True)

    document = Field(DocumentType)
        
    @classmethod
    def mutate(cls, root, info, document_input):
        document = Document(
            value = document_input.value
        )
        document.save()
        return CreateDocument(document=document)
    
class UpdateDocument(Mutation):
    
    class Arguments:
        document_input = DocumentInput(required=True)

    document = Field(DocumentType)
        
    @classmethod
    def mutate(cls, root, info, document_input):
        document = Document.objects.get(pk=document_input.id)
        document.value = document_input.value
        document.save()
        return UpdateDocument(document=document)

class Mutation(ObjectType):
    create_messagedocument = CreateDocument.Field()
    update_messagedocument = UpdateDocument.Field()
