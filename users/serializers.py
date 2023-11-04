from payment.serializers import PaymentSerializer
from users.models import User
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

# Serializers define the API representation.


class UserSerializer(serializers.ModelSerializer):
    pay_list = PaymentSerializer(source='payment_set', many=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'country', 'city', 'is_active', 'pay_list']  # Указываем поля для сериализации


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Добавление пользовательских полей в токен
        token['username'] = user.username
        token['email'] = user.email

        return token
