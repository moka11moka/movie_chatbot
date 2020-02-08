from django.shortcuts import render
from dashboard.constants import Template


def home_view(request):
    return render(request, Template.HOME, dict())
