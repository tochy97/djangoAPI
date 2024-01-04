from django.shortcuts import render
from django.template import RequestContext
from django.views.decorators.csrf import ensure_csrf_cookie

@ensure_csrf_cookie
def home(response):
    context = {'csrf_token': RequestContext}
    return render(response, "templates/index.html", context)

# def csrf_failure(request, reason=""):