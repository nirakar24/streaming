from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('series/<int:series_id>/', views.series_detail, name='series_detail'),
]

