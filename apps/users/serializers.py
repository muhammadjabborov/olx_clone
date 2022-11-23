from django.contrib.auth.hashers import make_password
from django.db.transaction import atomic
from rest_framework.exceptions import ValidationError
from rest_framework.fields import CharField, EmailField
from rest_framework.serializers import Serializer

from apps.users.models import User


class RegistrationSerializer(Serializer):
    full_name = CharField(max_length=255)
    username = CharField(max_length=255)
    password = CharField(max_length=255)
    email = EmailField(max_length=255)
    phone = CharField(max_length=25)
    confirm_password = CharField(max_length=255, write_only=True)

    def validate(self, data):
        if User.objects.filter(username=data['username']).exists():
            raise ValidationError("This username already taken")
        if data['password'] != data['confirm_password']:
            raise ValidationError({'password': 'Password fields did not match'})
        return data

    @atomic
    def create(self, validated_data):
        validated_data.pop('confirm_password')
        validated_data['password'] = make_password(validated_data['password'])
        user = User(**validated_data)
        user.save()
        return user

    class Meta:
        model = User
        fields = ['id', 'full_name', 'username', 'email', 'phone', 'password']
