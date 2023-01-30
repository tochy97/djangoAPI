from email import message
from re import sub
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.models import User
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import permissions, status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from django.conf import settings
from django.core.mail import send_mail
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from .models import Post, Day, Data
from .serializer import UserSerializer, UserSerializerWithToken, PostSerializer, DaySerializer, DataSerializer
from .permissions import IsOwner


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permissions_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = UserSerializer


class DayViewSet(viewsets.ModelViewSet):
    queryset = Day.objects.all()
    permissions_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = DaySerializer


class DataViewSet(viewsets.ModelViewSet):
    queryset = Data.objects.all()
    permissions_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = DataSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    permissions_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = PostSerializer


@api_view(['PATCH'])
@permission_classes([IsOwner])
def modify_user(request):
    queryset = User.objects.all()
    user = get_object_or_404(queryset, pk=request.user)
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def send_email(request):
    data = dict(request.data)
    data = list(data.keys())[0].split(",")
    for element in data:
        if(str(element).find("subject") > 0):
            subject = str(element).split(":")[1]
        if(str(element).find("message") > 0):
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


@api_view(['GET'])
def current_user(request):
    serializer = UserSerializer(request.user)
    return Response(serializer.data)


class CreateUser(APIView):

    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
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
