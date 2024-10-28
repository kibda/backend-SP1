from django.shortcuts import render
from django.http import JsonResponse
from .models import Artist
from artist.serializer import ArtistSerializer
from django.views.decorators.csrf import csrf_exempt

import json

@csrf_exempt
def create_artist_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format."}, status=400)

        name = data.get('name')
        biography = data.get('biography', "")
        date_of_birth = data.get('date_of_birth')
        country_of_origin = data.get('country_of_origin', "")
        style = data.get('style', "")

        if not name:
            return JsonResponse({"error": "Name is required."}, status=400)

        artist = Artist.objects.create(
            name=name,
            biography=biography,
            date_of_birth=date_of_birth,
            country_of_origin=country_of_origin,
            style=style,
            total_votes=0
        )

        artist_data = ArtistSerializer(artist).data
        return JsonResponse({"message": "Artist created successfully!", "artist": artist_data})
    else:
        return JsonResponse({"error": "Only POST requests are allowed."}, status=400)


def get_artist_view(request, artist_id):
    if request.method == 'GET':
        try:
            artist = Artist.objects.get(id=artist_id)
            artist_data = ArtistSerializer(artist).data
            return JsonResponse({"artist": artist_data})
        except Artist.DoesNotExist:
            return JsonResponse({"error": "Artist not found."}, status=404)
    else:
        return JsonResponse({"error": "Only GET requests are allowed."}, status=400)
   


def get_all_artists_view(request):
    if request.method == 'GET':
        artists = Artist.objects.all()
        artist_data = ArtistSerializer(artists, many=True).data
        return JsonResponse({"artists": artist_data})
    else:
        return JsonResponse({"error": "Only GET requests are allowed."}, status=400)
    


@csrf_exempt
def delete_artist_view(request, artist_id):
    if request.method == 'DELETE':
        try:
            artist = Artist.objects.get(id=artist_id)
            artist.delete()
            return JsonResponse({"message": "Artist deleted successfully!"})
        except Artist.DoesNotExist:
            return JsonResponse({"error": "Artist not found."}, status=404)
    else:
        return JsonResponse({"error": "Only DELETE requests are allowed."}, status=400)