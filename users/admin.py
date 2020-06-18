from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """ Custom User Admin"""

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {"fields": ("프로필_사진", "성별", "기타사항", "language", "통화", "할인_혜택_회원", "생일",)},
        ),
    )
