from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime

from .hash import  NewUser, CheckUser
from .forms import LoginForm, RegisterForm
from .schema import schema

# Create your views here.

@api_view(['POST'])
def auth(request):
    output = Response()
    form = LoginForm(request.data)
    if form.is_valid():
        output.data = CheckUser(request.data)
        output.status = 200
    else:
        output.data = "A field is missing."
        output.status = 700
    return output

@api_view(['POST'])
def register(request):
    output = Response()
    print(request.data)
    form = RegisterForm(request.data)
    if form.is_valid():
        output.data = NewUser(request.data)
        output.status = 200
    else:
        output.data = "A field is missing."
        output.status = 700
    return output