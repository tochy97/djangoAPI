from django.shortcuts import render
from django.template import RequestContext

def home(response):
    context = {'csrf_token': RequestContext}
    return render(response, "templates/index.html", context)

# def csrf_failure(request, reason=""):