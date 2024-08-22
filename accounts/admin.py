
# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm

    model = User

    list_display = ('email', 'is_active',
                    'is_staff', 'is_superuser','is_security','is_sdc',  'is_senate', 'last_login',  )
    list_filter = ('is_active', 'is_staff', 'is_superuser', 'is_security','is_sdc',  'is_senate',)
    fieldsets = (
        (None, {'fields': ('email', 'password', 'is_security','is_sdc',  'is_senate')}),
        ('Permissions', {'fields': ('is_staff', 'is_active',
         'is_superuser', 'groups', 'user_permissions')}),
        ('Dates', {'fields': ('last_login', 'date_joined')})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active', 'is_security', 'is_sdc', 'is_senate')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)

admin.site.register(User, CustomUserAdmin)