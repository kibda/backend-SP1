from django.db import models

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=100)
    biography = models.TextField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    country_of_origin = models.CharField(max_length=50, blank=True, null=True)
    style = models.CharField(max_length=50, blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    total_votes = models.IntegerField(default=0)

    def __str__(self):
        return self.name