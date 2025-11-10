from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from api import serializers as user_s
from rest_framework.response import Response
from rest_framework import status
#импорт модели пользователя
User = get_user_model()

#view для регестрации нового пользователя
class RegistrationView(CreateAPIView): #используеться готовая модель View где прописаны все запросы
    queryset = User.objects.all()
    permission_classes = [AllowAny] #разрешение на регистрацию всех пользователей
    serializer_class = user_s.RegistrationSerializer
    
class ChangePasswordView(APIView): #используеться самый базвый класс View, где нужно прописывать все запросы
    def post(self, request):
        user = request.user
        serializer = user_s.ChangePasswordSerializer(
            isinstance=user,
            data=request.data
            )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
    