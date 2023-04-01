from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from .views import home, current_user, create_user, modify_user, send_email

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('cjAPI/', include('cjAPI.urls')),
    path('okechAPI/', include('okechAPI.urls')),
    path("", home, name="home"),
    path('auth/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('currentuser/', current_user),
    path('createuser/', create_user),
    path('sendemail/', send_email),
    path('modifyuser/', modify_user)
]
