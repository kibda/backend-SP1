# ARTIST/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_artist_view, name='create_artist'),
    path('artist/<int:artist_id>/',  views.get_artist_view, name='get_artist'), 
    path('', views.get_all_artists_view, name='get_all_artists'),
    path('artist/delete/<int:artist_id>/', views.delete_artist_view, name='delete_artist')
]
