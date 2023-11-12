from django.urls import path
from rest_framework import routers, urlpatterns
from .views import PostListView, DayListView, DataListView, QuoteListView

urlpatterns = [
    path('post/', PostListView.as_view()),
    path('day/', DayListView.as_view()),
    path('data/', DataListView.as_view()),
    path('quote/', QuoteListView.as_view())
]

