from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from .views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('cjAPI/', include('cjAPI.urls')),
    path('okechAPI/', include('okechAPI.urls')),
    path("", home, name="home"),
    path('auth/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
