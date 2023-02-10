from django.contrib import admin
from . import models
from django.contrib.auth.models import Group
from .models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'created_at', 'updated_at', 'is_staff', 'is_active')
    search_fields = ('email', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.unregister(Group)