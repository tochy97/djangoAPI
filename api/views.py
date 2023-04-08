from email import message
from re import sub
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from django.conf import settings
from django.core.mail import send_mail
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from .models import Post, Day, Data, Quote
from .serializer import UserSerializer, UserSerializerWithToken, PostSerializer, DaySerializer, DataSerializer, QuoteSerializer

@api_view(['GET'])
@permission_classes([AllowAny])
def all_quotes(request):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer(queryset,many=True)
    quote_list = []
    for record in serializer_class.data:
        id = record['id']
        origin = record['origin']
        text = record['text']
        quote_list.append({"id":id,"origin":origin, "text":text})
    return Response(quote_list)

@api_view(['POST'])
@permission_classes([IsAdminUser])
def add_quote(request):
    serializer = QuoteSerializer(request.quote)
    if serializer.is_valid():
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH'])
@permission_classes([IsAdminUser])
def modify_quote(request):
    queryset = Quote.objects.all()
    quote = get_object_or_404(queryset, pk=request.user)
    serializer = QuoteSerializer(data=request.data)
    if serializer.is_valid():
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
