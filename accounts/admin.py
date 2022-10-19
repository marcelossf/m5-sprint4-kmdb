from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    readonly_fields = (["updated_at"])
    fieldsets = (
        ("Credenciais", {"fields": ("username", "password", "email", "birthdate")}),
        (
            "Personal Info",
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "bio",
                    "is_critic",
                )
            },
        ),
        ("Permissions", {"fields": ("is_staff", "is_superuser")}),
    )

admin.site.register(User, CustomUserAdmin)