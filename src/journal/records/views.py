from django.views.generic import DetailView, ListView

from .models import Record


class RecordDetailView(DetailView):
    model = Record


class RecordListView(ListView):
    model = Record
    paginate_by = 10
    queryset = Record.objects.all().order_by("created_at")
