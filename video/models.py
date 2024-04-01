from django.db import models

# Create your models here.
# models.py

from django.db import models

class Series(models.Model):
    title = models.CharField(max_length=100)
    poster = models.ImageField(upload_to='posters/')
    posterbg = models.ImageField(upload_to='posters_bg/')
    # Add any other fields you need for your Series model

    def __str__(self):
        return self.title

class Episode(models.Model):
    series = models.ForeignKey(Series, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    video_url = models.URLField()
    # Add any other fields you need for your Episode model

    def __str__(self):
        return f"{self.series.title} - {self.title}"

