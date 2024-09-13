from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from diary.forms import EntryForm
from diary.models import Entry


class SearchEntryListView(ListView):
    """Контроллер поиска"""

    model = Entry

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        text_search = self.request.GET.get("search")
        if text_search is None or not text_search:
            context["object_list"] = Entry.objects.all()
        else:
            context["object_list"] = Entry.objects.filter(
                Q(title__contains=text_search) | Q(content__contains=text_search))
        return context


class EntryListView(ListView):
    """Контроллер отображения всех записей дневника"""

    model = Entry

    # def get_queryset(self):
    #     return Entry.objects.filter(owner=self.request.user)


class EntryDetailView(DetailView):
    """Контроллер подробного отображения одной записи дневника"""

    model = Entry

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


class EntryCreateView(CreateView, LoginRequiredMixin):
    """Контроллер создания одной записи дневника"""

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
    """Контроллер для внесения изменений одной записи дневника"""

    model = Entry
    form_class = EntryForm
    success_url = reverse_lazy("diary:entry_list")

    def get_success_url(self):
        return reverse('diary:entry_detail', args=[self.kwargs.get('pk')])


class EntryDeleteView(LoginRequiredMixin, DeleteView):
    """Контроллер удаления одной записи дневника"""

    model = Entry
    success_url = reverse_lazy("diary:entry_list")


def top(request):
    """Функция отображения главной страницы"""

    return render(request, "diary/top.html")
