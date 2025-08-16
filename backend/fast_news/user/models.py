from django.db import models


class User(models.Model):
    username = models.CharField(
        max_length=100,
        help_text="user_name",
    )
    email = models.EmailField(
        unique=True,
        help_text="user_email",
    )
    first_name = models.CharField(
        max_length=100, blank=True, null=True, help_text="first_name"
    )
    last_name = models.CharField(
        max_length=100, help_text="last_name", blank=True, null=True
    )
    password = models.CharField(max_length=100, help_text="password")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # class Meta:
    #     ordering = ("-created_at",)
