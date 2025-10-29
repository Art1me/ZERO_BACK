from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from api.managers import CustomBaseManager
#Создание класса пользователя с использованием AbstractUser
class User(AbstractUser):
    phone_number = PhoneNumberField('Телефон',unique=True)
    birth_data = models.DateField('Дата рождения')
    place_of_work = models.CharField('Место работы', max_length=100)
    
    #USERNAME_FIELD = ''
    #REQUIRED_FIELDS = ''
    
    objects = CustomBaseManager()
    
    
    class Meta:
        verbose_name = 'Польззователь'
        verbose_name_plural = 'Пользователи'