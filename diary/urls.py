from django.urls import path, include
from diary.apps import DiaryConfig
from diary.views import entry_list, entry_detail

app_name = DiaryConfig.name

urlpatterns = [
    path("", entry_list, name="entry_list"),
    path("entrys/<int:pk>/", entry_detail, name="entry_detail"),
]
