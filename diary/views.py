from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from diary.forms import EntryForm
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


class EntryCreateView(CreateView, LoginRequiredMixin):
    model = Entry
    form_class = EntryForm
    success_url = reverse_lazy("diary:entry_list")

    def form_valid(self, form):
        entry = form.save()
        user = self.request.user
        entry.owner = user
        entry.save()
        return super().form_valid(form)


class EntryUpdateView(LoginRequiredMixin, UpdateView):
    model = Entry
    form_class = EntryForm
    success_url = reverse_lazy("diary:entry_list")

    def get_success_url(self):
        return reverse('diary:entry_detail', args=[self.kwargs.get('pk')])


class EntryDeleteView(LoginRequiredMixin, DeleteView):
    model = Entry
    success_url = reverse_lazy("diary:entry_list")
