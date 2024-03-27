# views.py

from django.shortcuts import render, get_object_or_404
from .models import Series, Episode

def home(request):
    series = Series.objects.all()
    return render(request, 'home.html', {'series': series})

def series_detail(request, series_id):
    series = get_object_or_404(Series, pk=series_id)
    episodes = Episode.objects.filter(series=series)
    return render(request, 'series_detail.html', {'series': series, 'episodes': episodes})
