from django.contrib import admin
from diary.models import Entry

"""Настройка отображения модели Запись в администрации приложения"""


@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'created_at']
    list_filter = ['title', 'created_at']
