from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'is_staff',
            'email',
            'first_name',
            'last_name',
            'username',
            'id'
        ]
