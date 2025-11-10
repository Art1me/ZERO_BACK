from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.exceptions import ParseError
from django.contrib.auth.password_validation import validate_password


#импорт модели пользователя
User = get_user_model()

##############################################################
# Создание среиализатора для регестрации нового пользователя #
##############################################################  
class RegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField() #поле для ввода почты
    password = serializers.CharField(write_only=True) #write_only=True - поле для отправки пароля, но не для ввода в форму
        
    #обязательные поля ввода для регистрации
    class Meta:
        model = User
        fields = (
            'id', #не вводиться в форму, автоматичекаское поле
            'email',
            'first_name',
            'last_name',
            'surname',
            'phone_number',
            'birthday',
            'password',
        )
        
    #функция для обработки поля "Почта"
    def validate_email(self, value):
        email = value.lower() #приведение почты к нижнему регистру
        if User.objects.filter(email=email).exists():
            raise ParseError(
                'Пользователь с такой почтой уже существует'
            )
        return email
    
    #функция для обработки поля "Пороль"    
    def validate_password(self, value):
        validate_password(value)
        return value
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

############################################################
# Создание среиализатора для изменения пароля пользователя #
############################################################
class ChangePasswordSerializer(serializers.ModelSerializer):
    old_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = (
            'old_password',
            'new_password',
        )
    
    def validate(self, attrs):
        user = attrs.instance
        old_password = attrs.pop('old_password')
        if not user.check_password(old_password):
            raise ParseError(
                'Новый пороль не являеться коректным'
            )
        return attrs
        
    def update(self, instance, validated_data):
        password = validated_data.pop('new_password')
        instance.set_password(password)
        instance.save()
        return instance

###########################################################    
# Создание среиализатора для изменения email пользователя #
###########################################################
class ChangeEmailSerializer(serializers.Serializer):
    new_email = serializers.EmailField(required=True)
    
    def validate_new_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Пользователь с таким email уже существует.")
        return value

    def update(self, user, validated_data):
        new_email = validated_data.get('new_email')
        user.email = new_email
        user.save()
        return user

#####################################################################
# Создание среиализатора для изменения номера телефона пользователя #
#####################################################################
class ChangePhoneNumberSerializer(serializers.Serializer):
    new_phone_number = serializers.CharField(required=True)

    def validate_new_phone_number(self, value):
        if User.objects.filter(phone_number=value).exists():
            raise serializers.ValidationError("Пользователь с таким номером телефона уже существует.")
        return value

    def update(self, user, validated_data):
        new_phone_number = validated_data.get('new_phone_number')
        user.phone_number = new_phone_number
        user.save()
        return user