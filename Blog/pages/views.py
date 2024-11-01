from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from .models import Notee


class HomePage(ListView):
    template_name = "home.html"
    queryset = Notee.objects.all()

class AboutPage(TemplateView):
    template_name = "about.html"