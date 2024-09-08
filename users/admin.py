from django.contrib import admin

from users.models import User

"""Настройка отображения модели Запись в администрации приложения"""


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "email"]
