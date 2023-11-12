from rest_framework import generics
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView

from school.permissions import IsSuperuser
from users.models import User
from users.serializers import UserSerializer, MyTokenObtainPairSerializer


class UserAPIView(generics.CreateAPIView):
    def create(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():

            user = serializer.save(is_active=True)

            user.set_password(raw_password='password')
            user.save()


            return Response({'message': 'Пользователь успешно создан'})
        return Response(serializer.errors, status=400)




class UserListAPIView(ListAPIView):
    serializer_class = UserSerializer  # Указание сериализатора для обработки
    queryset = User.objects.all()
    permission_classes = [IsSuperuser]


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
