from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField # type: ignore
from api.managers import CustomBaseManager



#Создание класса пользователя (User) с использованием AbstractUser
class User(AbstractUser):
    #поля для обязательных данных
    username = models.CharField('Имя пользователя', unique=True, max_length=150, null=True, blank=True)
    phone_number = PhoneNumberField('Телефон',unique=True, null = True)
    email = models.EmailField('Электронная почта', unique=True, null = True) 
    password = models.CharField('Пароль', max_length=128)
    first_name = models.CharField('Имя', max_length=100,null = True)
    last_name = models.CharField('Фамилия', max_length=100,null = True)
    birthday = models.DateField('Дата рождения', null=True,)
    
    #поля для дополнительных данных
    place_of_work = models.CharField('Место работы', max_length=100,null = True,blank=True)
    
    #поля для проверки подтверждения аккаунта и корпоративного аккаунта
    is_verified = models.BooleanField('Подтвержден', default=True)
    is_corporate_account = models.BooleanField('Корпоративный аккаунт', default=False)
    
    
    #поля для администратора
    is_active = models.BooleanField('Активен', default=True)
    is_superuser = models.BooleanField('Суперпользователь', default=False)
    is_staff = models.BooleanField('Staff', default=False)
    
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    
    #наследование методов из CustomBaseManager
    objects = CustomBaseManager()
    
    
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        
    
    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    
    def __str__(self):
        return f'{self.full_name} ({self.pk})'
    
    