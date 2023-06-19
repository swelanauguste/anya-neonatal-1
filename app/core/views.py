from django.shortcuts import render
from django.views.generic import CreateView, ListView

from .forms import SpecialCareForm
from .models import SpecialCare


class SpecialCareCreateView(CreateView):
    model = SpecialCare
    form_class = SpecialCareForm


class SpecialCareListView(ListView):
    model = SpecialCare
