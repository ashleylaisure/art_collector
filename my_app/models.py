from django.db import models
from django.urls import reverse
from datetime import date

medium_choices = (
    ('oil', 'Oil Paint'),
    ('acrylic', 'Acrylic Paint'),
    ('watercolor', 'Watercolor'),
    ('gouache', 'Gouache'),
    ('pastels', 'Pastels'),
    ('ink', 'Ink'),
    ('graphite', 'Graphite/Charcoal'),
    ('color_pencils', 'Colored Pencils'),
    ('mixed_media', 'Mixed Media'),
)
    
movement_choices = (
    ('abstract', 'Abstract Expressionism'),
    ('art_deco', 'Art Deco'),
    ('art_nouveau', 'Art Nouveau'),
    ('baroque', 'Baroque'),
    ('classicism', 'Classicism'),
    ('contemporary', 'Contemporary Art'),
    ('cubism','Cubism'),
    ('expressionism', 'Expressionism'),
    ('realism', 'Hyperrealism'),
    ('renaissance', 'Renaissance'),
    ('impressionism', 'Impressionism'),
    ('modern', 'Modern Art'),
    ('neoclassicism', 'Neoclassicism'),
    ('pop', 'Pop Art'),
    ('rococo', 'Rococo'),
    ('surrealism', 'Surrealism'),
)
# Create your models here.
class Art(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    date = models.CharField('Year Completed', max_length=50)
    medium = models.CharField(max_length=100, choices=medium_choices)
    movement = models.CharField(max_length=100, choices=movement_choices)
    location = models.CharField(max_length=200, default="unknown")
    viewed = models.BooleanField("Viewed in Person", default=False)
    image = models.URLField(max_length=200)
    
    def __str__(self):
        return self.title
    
    # Define a method to get the URL for this particular instance
    def get_absolute_url(self):
        # Use the 'reverse' function to dynamically find the URL for viewing this models's details
        return reverse("art-detail", kwargs={'art_id': self.id})
    
    
class Copy(models.Model):
    artwork = models.ForeignKey(Art, on_delete=models.CASCADE)
    artist = models.CharField(max_length=100)
    date = models.DateField('Date Painted', default=date.today)
    notes = models.TextField(max_length=250)
    image = models.URLField(max_length=200)
    
    
    def __str__(self):
        return self.artist