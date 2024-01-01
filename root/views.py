from django.shortcuts import render
from django.shortcuts import  render

def home(response):
    return render(response, "templates/index.html", {})
