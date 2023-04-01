from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from django.utils.translation import gettext_lazy as _
from .models import Post, Day, Data, Quote


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


class QuoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Quote
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'


class DataSerializer(serializers.ModelSerializer):

    class Meta:
        model = Data
        fields = '__all__'


class DaySerializer(serializers.ModelSerializer):

    class Meta:
        model = Day
        fields = '__all__'


class UserSerializerWithToken(serializers.ModelSerializer):

    token = serializers.SerializerMethodField()
    password = serializers.CharField(write_only=True)

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
