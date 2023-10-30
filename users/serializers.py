from django.contrib.auth.models import User
from rest_framework import serializers

# Serializers define the API representation.


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'country', 'city', 'is_active']  # Указываем поля для сериализации
