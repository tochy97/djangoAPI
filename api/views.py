from django.views.generic import ListView
from .models import Post, Day, Data, Quote
from .serializer import UserSerializer, UserSerializerWithToken, PostSerializer, DaySerializer, DataSerializer, QuoteSerializer

class PostListView(ListView):
    model = Post


class DayListView(ListView):
    model = Day


class DataListView(ListView):
    model = Data


class QuoteListView(ListView):
    model = Quote
