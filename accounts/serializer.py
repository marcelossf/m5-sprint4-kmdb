from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=20, validators=[UniqueValidator(queryset=User.objects.all(), message="Username já utilizado")])
    email = serializers.EmailField(max_length=127, validators=[UniqueValidator(queryset=User.objects.all(), message="E-mail já cadastrado")])
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    birthdate = serializers.DateField()
    bio = serializers.CharField(default="")
    is_critic = serializers.BooleanField(default=False)
    updated_at = serializers.DateTimeField(read_only=True)
    is_superuser =serializers.BooleanField(read_only=True)

    def create(self, validated_data):
        newUser = User.objects.get_or_create(**validated_data)

        return newUser