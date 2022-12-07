# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Local
from .forms import (
    ClientChangeForm,
    ClientCreationForm
)
from .models import Client


class ClientAdmin(UserAdmin):
    add_form = ClientCreationForm
    form = ClientChangeForm
    model = Client

    fieldsets = (
        ('Information', {
            'fields': (
                'email',
                'password',
                'date_joined',
                'balance'
            )
        }),
        ('Permissions', {
            'fields': (
                'is_superuser',
                'is_staff',
                'is_active'
            )
        })
    )
    add_fieldsets = (
        (None, {
            'classes': (
                'wide',
            ),
            'fields': (
                'email',
                'password1',
                'password2',
                'is_active'
            ),
        }),
    )
    search_fields = (
        'email',
    )
    readonly_fields = (
        'date_joined',
        'is_superuser',
        'is_staff',
        'is_active',
        'balance'
    )
    list_display = (
        'email',
        'password',
        'date_joined',
        'is_superuser',
        'is_staff',
        'is_active',
        'balance'
    )
    list_filter = (
        'is_superuser',
        'is_staff',
        'is_active'
    )
    ordering = (
        'email',
    )


admin.site.register(Client, ClientAdmin)