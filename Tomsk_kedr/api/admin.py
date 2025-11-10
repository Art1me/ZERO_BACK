from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from api.models.users import User
from django.utils.translation import gettext_lazy as _

@admin.register(User)
class UserAdmin(UserAdmin):
    change_user_password_template = None
    fieldsets = (
        (None, {'fields': ('phone_number', 'email', 'username',)}),
        (_('Личная информация'),
         {'fields': ('first_name', 'last_name', 'surname','birthday',)}), #!!!!!!!! также будет добавленно 'place_of_work' !!!!!
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'phone_number','first_name','last_name','surname','birthday', 'password1', 'password2',),
        }),
    )
    list_display = ('id', 'full_name', 'email', 'phone_number', 'is_active', 'is_staff', 'is_superuser', )

    list_display_links = ('id', 'full_name',)
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    search_fields = ('first_name', 'last_name', 'id', 'email', 'phone_number',)
    ordering = ('-id',)
    filter_horizontal = ('user_permissions',)
    readonly_fields = ('last_login',)

    