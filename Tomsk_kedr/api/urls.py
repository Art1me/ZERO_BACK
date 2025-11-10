from django.urls import path, include
from api import views



urlpaterns = [
    path('api/registration/', views.RegistrationView.as_view(), name='registration'),   # регистрация нового пользователя
    path('api/change-password/', views.ChangePasswordView.as_view(), name='change-password'), # изменение пароля пользователя
    path('api/djoser-auth/', include('djoser.urls')), # вход пользователя
    path('api/auth/', include('rest_framework.urls')),#+ login/ или  logout/  вход и выход из учетки
]