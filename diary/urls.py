from django.urls import path
from diary.apps import DiaryConfig
from diary.views import EntryListView, EntryDetailView, EntryCreateView, EntryUpdateView, EntryDeleteView, about, base, \
    SearchEntryListView

app_name = DiaryConfig.name

urlpatterns = [
    path("", base, name="base"),
    path("entrys/", EntryListView.as_view(), name="entry_list"),
    path("entrys/<int:pk>/", EntryDetailView.as_view(), name="entry_detail"),
    path("entrys/create", EntryCreateView.as_view(), name="entry_create"),
    path("entrys/<int:pk>/update/", EntryUpdateView.as_view(), name="entry_update"),
    path("entrys/<int:pk>/delete/", EntryDeleteView.as_view(), name="entry_delete"),
    path("about/", about, name="about"),
    path("search/", SearchEntryListView.as_view(), name="search"),
]
