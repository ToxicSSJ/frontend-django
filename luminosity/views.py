from django.shortcuts import render

# Vista de inicio
# o punto de partida
# del front-end.
# from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic import TemplateView

class StartView(TemplateView):
    template_name = 'index.html'