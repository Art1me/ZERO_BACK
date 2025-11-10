from django.contrib.auth.models import BaseUserManager
from rest_framework.exceptions import ParseError


class CustomBaseManager(BaseUserManager):
    use_in_migrations = True 
    
    def _create_user(self,phone_number = None, email = None, password = None, username = None, birthday = None, **extra_fields):
        if not(email or phone_number):
            raise ParseError('Укажите почту или номер телефона')
        
        if email:
            email = self.normalize_email(email)
        
        if not username:
            if email:
                username = email
            else:
                username = phone_number
        
        user = self.model(username=username, birthday=birthday, **extra_fields)        
        if email:
            user.email = email
        if phone_number:
            user.phone_number = phone_number
        
        
        user.set_password(password)
        user.save(using = self.db)
        return user

    def create_user(self, phone_number = None, email = None, password = None, username = None, birthday = None,**extra_fields):
        # Для обычных пользователей проверяем birthday
        if not birthday:
            raise ValueError('Дата рождения обязательна для обычных пользователей')
        
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_active', True)
        
        return self._create_user(
            phone_number, email, password, username, birthday, **extra_fields
                                 )

    
    def create_superuser(self,phone_number = None, email = None, password = None, username = None, birthday=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)

        return self._create_user(
            phone_number, email, password, username, birthday, **extra_fields
            )