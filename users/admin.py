from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Настройка отображения модели Запись в администрации приложения"""

    list_display = ["id", "email"]
