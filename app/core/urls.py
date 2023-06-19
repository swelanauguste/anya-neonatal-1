from django.urls import path

from .views import SpecialCareCreateView, SpecialCareListView

urlpatterns = [
    path("", SpecialCareCreateView.as_view(), name="specialcare-create"),
    path("list/", SpecialCareListView.as_view(), name="specialcare-list"),
]
