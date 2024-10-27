# ARTIST/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_artist_view, name='create_artist'),
    path('<int:artist_id>/',  views.get_artist_view, name='get_artist'), 
]
