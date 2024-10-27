from django.shortcuts import render
from django.http import JsonResponse
from .models import Artist
from artist.serializer import ArtistSerializer

def create_artist_view(request):
    if request.method == 'POST':
        data = request.POST
        name = data.get('name')
        biography = data.get('biography', "")
        date_of_birth = data.get('date_of_birth')
        country_of_origin = data.get('country_of_origin', "")
        style = data.get('style', "")
        
        # Create and save the artist instance directly in the view
        artist = Artist.objects.create(
            name=name,
            biography=biography,
            date_of_birth=date_of_birth,
            country_of_origin=country_of_origin,
            style=style,
            total_votes=0
        )
        
        # Serialize the created artist (if needed)
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
   