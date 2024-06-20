from django.urls import path

from . import views

urlpatterns = [
    path(
        "",
        views.RecordListView.as_view(),
        name="records"
    ),
    path(
        "record/<int:pk>",
        views.RecordDetailView.as_view(),
        name="record-details"
    ),
]