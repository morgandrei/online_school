from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

from users.models import User
from users.serializers import UserSerializer, MyTokenObtainPairSerializer

from rest_framework_simplejwt.views import TokenObtainPairView


class UserAPIView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({'message': 'Пользователь успешно создан'})
        return Response(serializer.errors, status=400)


class UserListAPIView(ListAPIView):
    serializer_class = UserSerializer  # Указание сериализатора для обработки
    queryset = User.objects.all()


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
