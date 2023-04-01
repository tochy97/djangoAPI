from django.urls import path
from rest_framework import routers, urlpatterns
from .views import all_quotes, modify_quote, add_quote

router = routers.DefaultRouter()


urlpatterns = [
    path('allquotes/', all_quotes),
    path('modifyquote/', modify_quote),
    path('addquote/', add_quote)
]

urlpatterns += router.urls
