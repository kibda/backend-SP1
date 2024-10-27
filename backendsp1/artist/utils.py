from .models import Artist

def create_artist(name, biography="", date_of_birth=None, country_of_origin="", style="", profile_picture=None, rating=0, popularity_score=0, is_featured=False):
    # Create a new Artist instance
    artist = Artist(
        name=name,
        biography=biography,
        date_of_birth=date_of_birth,
        country_of_origin=country_of_origin,
        style=style,
        profile_picture=profile_picture,
        rating=rating,
        popularity_score=popularity_score,
        is_featured=is_featured
    )
    # Save the artist to the database
    artist.save()
    return artist