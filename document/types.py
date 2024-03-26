from graphene_django import DjangoObjectType
from django.contrib.auth.models import User

from .models import Document

class DocumentType(DjangoObjectType):
    class Meta:
        model = Document
        fields = '__all__'