from django.db import models

# Create your models here.
class Art(models.Model):
    medium_choices = [
        ('oil', 'Oil Paint'),
        ('acrylic', 'Acrylic Paint'),
        ('watercolor', 'Watercolor'),
        ('gouache', 'Gouache'),
        ('pastels', 'Pastels'),
        ('ink', 'Ink'),
        ('graphite', 'Graphite/Charcoal'),
        ('color_pencils', 'Colored Pencils'),
        ('mixed_media', 'Mixed Media'),
    ]
    
    movement_choices = [
        ('abstract', 'Abstract Expressionism'),
        ('art_deco', 'Art Deco'),
        ('art_nouveau', 'Art Nouveau'),
        ('baroque', 'Baroque'),
        ('classicism', 'Classicism'),
        ('contemporary', 'Contemporary Art'),
        ('cubism','Cubism'),
        ('expressionism', 'Expressionism'),
        ('realism', 'Hyperrealism'),
        ('impressionism', 'Impressionism'),
        ('modern', 'Modern Art'),
        ('neoclassicism', 'Neoclassicism'),
        ('pop', 'Pop Art'),
        ('rococo', 'Rococo'),
        ('surrealism', 'Surrealism'),
    ]
    
    
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    date = models.CharField(max_length=50)
    medium = models.CharField(max_length=100, choices=medium_choices, default="oil")
    movement = models.CharField(max_length=100, choices=movement_choices)
    image = models.URLField(max_length=200)
    
    def __str__(self):
        return self.title