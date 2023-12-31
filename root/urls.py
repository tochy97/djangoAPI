from django.contrib import admin
from django.urls import path, include
from .views import home, send_email

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path("", home, name="home"),
    path('sendemail/', send_email),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
]
