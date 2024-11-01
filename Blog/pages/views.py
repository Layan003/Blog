from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

class HomePage(TemplateView):
    template_name = "home.html"

class AboutPage(TemplateView):
    template_name = "about.html"