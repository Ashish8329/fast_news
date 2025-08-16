from django.contrib import admin

from .models import User


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fields = (
        "username",
        "email",
        "first_name",
        "last_name",
        "password",
        "created_at",
        "updated_at",
    )
    readonly_fields = ["created_at", "updated_at"]
