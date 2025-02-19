from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'full_name', 'company', 'phone')
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('full_name', 'company', 'address', 'city', 
                                      'postal_code', 'phone', 'country')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)