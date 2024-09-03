from django.urls import path, include
from diary.apps import DiaryConfig
from diary.views import EntryListView, EntryDetailView, EntryCreateView

app_name = DiaryConfig.name

urlpatterns = [
    path("", EntryListView.as_view(), name="entry_list"),
    path("entrys/<int:pk>/", EntryDetailView.as_view(), name="entry_detail"),
    path("entrys/create", EntryCreateView.as_view(), name="entry_create"),
]
