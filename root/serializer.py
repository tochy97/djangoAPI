from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

class UserSerializerWithToken(serializers.ModelSerializer):
    
    def get_tokens_for_user(user):
        refresh = RefreshToken.for_user(user)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    class Meta:
        model = User
        fields = [('token', 'username', 'password',
                   ), 'first_name', 'last_name', 'email']


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
