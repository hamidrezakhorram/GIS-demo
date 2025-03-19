from django.contrib import admin
from .models import User, Profile
from django.contrib.auth.admin import UserAdmin

class CustomUserAmin(UserAdmin):
    model = User
    list_display = ("phone_number", "is_staff", "is_active")
    list_filter = ("phone_number", "is_staff", "is_active")
    search_fields = ("phone_number",)
    ordering = ("phone_number",)
    fieldsets = (
        ("Authenticate", {"fields": ("phone_number",)}),
        (
            "permissions",
            {
                "fields": (
                    "is_active",
                    'is_superuser',
                    "is_staff",
                    'groups',
                    'user_permissions',
                    
                )
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "phone_number",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                    
                   
                ),
            },
        ),
    )

admin.site.register(User, CustomUserAmin)
admin.site.register(Profile)
