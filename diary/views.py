from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from diary.models import Entry


class EntryListView(ListView):
    model = Entry


class EntryDetailView(DetailView):
    model = Entry

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


class EntryCreateView(CreateView):
    model = Entry
    fields = ("title", "content", "image", "publication_sign")
    success_url = reverse_lazy("diary:entry_list")


class EntryUpdateView(UpdateView):
    model = Entry
    fields = ("title", "content", "image", "publication_sign")
    success_url = reverse_lazy("diary:entry_list")

    def get_success_url(self):
        return reverse('diary:entry_detail', args=[self.kwargs.get('pk')])


class EntryDeleteView(DeleteView):
    model = Entry
    success_url = reverse_lazy("diary:entry_list")
