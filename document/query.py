from graphene import ObjectType, Field, Int, List
from graphql_auth.schema import UserQuery, MeQuery 
from django.contrib.auth.models import User

from .models import Document
from .types import DocumentType
        
class Query(UserQuery, MeQuery, ObjectType):
    
    get_Document = Field(DocumentType, id=Int())
    def resolve_get_Document(root, info, id):
        return Document.objects.get(pk=id)