from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from diary.models import Entry


class EntryListView(ListView):
    model = Entry


class EntryDetailView(DetailView):
    model = Entry


class EntryCreateView(CreateView):
    model = Entry
    fields = ("title", "content", "image", "publication_sign", "number_of_views")
    success_url = reverse_lazy("diary:entry_list")
