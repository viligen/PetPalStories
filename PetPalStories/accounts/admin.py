from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from PetPalStories.accounts.forms import UserEditForm, UserCreateForm

UserModel = get_user_model()


@admin.register(UserModel)
class AppUserAdmin(UserAdmin):
    form = UserEditForm
    add_form = UserCreateForm

    fieldsets = (
        (
            None,
            {
                'fields': (
                    'username',
                    'password',
                ),
            }),
        (
            'Personal info',
            {
                'fields': (
                    'first_name',
                    'last_name',
                    'email',
                    'gender'
                ),
            },
        ),
        (
            'Permissions',
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                    'groups',
                    'user_permissions',
                ),
            },
        ),
        (
            'Important dates',
            {
                'fields': (
                    'last_login',
                    'date_joined',
                ),
            },
        ),
    )

    def get_form(self, request, obj=None, **kwargs):
        return super().get_form(request, obj, **kwargs)