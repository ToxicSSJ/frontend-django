from django.shortcuts import render
import requests

# Vista de inicio
# o punto de partida
# del front-end.
# from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic import TemplateView

def luminosity(request):
    if 'value' in request.GET:
        value = request.GET['value']
        latitude = request.GET['latitude']
        length = request.GET['length']
        terrain = request.GET['terrain']
        if value:
            args = {'type': 'number', 'value': value, 'latitude': latitude, 'length': length, 'terrain': terrain}
            response = requests.post('http://127.0.0.1:8000/luminosity/', args)
            measure_json = response.json()
    response = requests.get('http://127.0.0.1:8000/luminosity/')
    entries = response.json()
    return render(request, "luminosity.html", {'entries': entries})

#class StartView(TemplateView):
#    template_name = 'index.html'