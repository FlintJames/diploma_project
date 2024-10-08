from django.contrib import admin
from diary.models import Entry


@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    """Настройка отображения модели Запись в администрации приложения"""

    list_display = ['pk', 'title', 'created_at']
    list_filter = ['title', 'created_at']
