from django.db import models
from django.urls import reverse

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
    image = models.URLField(max_length=200)
    
    def __str__(self):
        return self.title
    
    # Define a method to get the URL for this particular instance
    def get_absolute_url(self):
        # Use the 'reverse' function to dynamically find the URL for viewing this models's details
        return reverse("art-detail", kwargs={'art_id': self.id})
    
    
class Viewing(models.Model):
    date = models.DateField()
    museum = models.CharField(max_length=200)
    
    art = models.ForeignKey(Art, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.museum} on {self.date}"