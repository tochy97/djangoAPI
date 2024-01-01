from django.urls import path
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt

from .schema import schema
from .views import auth, register

urlpatterns = [
    path("graphql", csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))),
]