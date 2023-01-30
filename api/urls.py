from django.urls import path
from rest_framework import routers, urlpatterns
from .views import PostViewSet, UserViewSet, DayViewSet, DataViewSet, current_user, CreateUser, modify_user, send_email

router = routers.DefaultRouter()

router.register('posts', PostViewSet, 'posts')
router.register('days', DayViewSet, 'days')
router.register('data', DataViewSet, 'data')
router.register('users', UserViewSet, 'users')

urlpatterns = [
    path('currentuser/', current_user),
    path('createuser/', CreateUser.as_view()),
    path('sendemail/', send_email),
    path('modifyuser/', modify_user),
]

urlpatterns += router.urls
