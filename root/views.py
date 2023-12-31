from django.shortcuts import render
from django.http import HttpResponse
from .serializer import UserSerializer
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
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.generics import RetrieveAPIView

def home(response):
    return render(response, "templates/index.html", {})

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
