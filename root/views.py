from django.shortcuts import render
from django.http import HttpResponse
from .serializer import UserSerializer, UserSerializerWithToken
from django.http import Http404
from django.conf import settings
from django.core.mail import send_mail
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from rest_framework.decorators import api_view
from re import sub
from django.shortcuts import get_object_or_404, render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.generics import RetrieveAPIView

def home(response):
    return render(response, "templates/index.html", {})

def get_user_from_access_token_in_django_rest_framework_simplejwt(access_token_str):
    access_token_obj = AccessToken(access_token_str)
    user_id = access_token_obj['user_id']
    user = User.objects.get(id=user_id)
    print('user_id: ', user_id)
    print('user: ', user)
    print('user.id: ', user.id)
    content = {'user_id': user_id, 'user': user, 'user.id': user.id}
    return Response(content)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def current_user(request):
    serializer = UserSerializer(request.user)
    return Response(serializer.data)

@api_view(['PATCH'])
@permission_classes([IsAdminUser])
def modify_user(request):
    queryset = User.objects.all()
    user = get_object_or_404(queryset, pk=request.user)
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny])
def send_email(request):
    data = dict(request.data)
    data = list(data.keys())[0].split(",")
    for element in data:
        if (str(element).find("subject") > 0):
            subject = str(element).split(":")[1]
        if (str(element).find("message") > 0):
            message = str(element).split(":")[1]
    return Response(
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [settings.EMAIL_HOST_USER],
            fail_silently=False,
        )
    )

@api_view(['POST'])
@permission_classes([AllowAny])
def create_user(request):
    serializer = UserSerializerWithToken(data=request.data)
    if serializer.is_valid():
        username = request.data.get('username', None)
        email = request.data.get('email', None)
        serializer.save()
        send_mail(
            'Welcome to tochyegeonu.com',
            f"Hello,  {username}.\nThank you for registering for my website and enjoy the tutorials.",
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
