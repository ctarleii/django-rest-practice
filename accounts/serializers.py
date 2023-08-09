from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer

from accounts.models import User


class SignUpSerializer(ModelSerializer):
    email = serializers.EmailField(max_length=80, min_length=4)
    username = serializers.CharField(max_length=45, min_length=4)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password']

    def validate(self, attrs):
        email_exists = User.objects.filter(email=attrs['email'])
        if email_exists:
            raise ValidationError("Email already exists")

        username_exists = User.objects.filter(username=attrs['username'])
        if username_exists:
            raise ValidationError("Username already exists")
        
        return super().validate(attrs)

    def create(self, validated_data):
        password = validated_data.pop('password')

        user = super().create(validated_data)
        user.set_password(password)
        user.save()

        Token.objects.create(user=user)

        return user


