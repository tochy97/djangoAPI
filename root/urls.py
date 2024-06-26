from django.contrib import admin
from django.urls import path, include
from graphene_django.views import GraphQLView

from .views import home
from .schema import schema

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home, name="home"),
    path("graphql", GraphQLView.as_view(graphiql=True, schema=schema)),
]
