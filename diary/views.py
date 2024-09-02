from django.shortcuts import render, get_object_or_404

from diary.models import Entry


def entry_list(request):
    entrys = Entry.objects.all()
    context = {"entrys": entrys}
    return render(request, "diary/entry_list.html", context)


def entry_detail(request, pk):
    entry = get_object_or_404(Entry, pk=pk)
    context = {"entry": entry}
    return render(request, "diary/entry_detail.html", context)
