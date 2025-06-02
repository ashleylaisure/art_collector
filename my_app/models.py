from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

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
    ('other', 'Other'),
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
color_choices = (
    ('aliceBlue', 'Alice Blue'),
    ('aquamarine', 'Aquamarine'),
    ('chartreuse', 'Chartreuse'),
    ('coral', 'Coral'),
    ('crimson', 'Crimson'),
    ('seaGree', 'Dark Sea Green'),
    ('deepPink','Deep Pink'),
    ('dodgerBlue', 'Dodger Blue'),
    ('slateGray', 'Slate Gray'),
    ('tomato', 'Tomato'),
)
# Create your models here.
class List(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20, choices=color_choices)
    notes = models.CharField(max_length=150)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("list-detail", kwargs={"pk": self.id})
    
class Art(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    date = models.CharField('Year Completed', max_length=50)
    medium = models.CharField(max_length=100, choices=medium_choices)
    movement = models.CharField(max_length=100, choices=movement_choices, blank=True, null=True)
    location = models.CharField(max_length=200, default="unknown")
    viewed = models.BooleanField("Viewed in Person", default=False)
    image = models.URLField(max_length=200)
    # Add the M:M relationship
    lists = models.ManyToManyField(List)
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
    # Define a method to get the URL for this particular instance
    def get_absolute_url(self):
        # Use the 'reverse' function to dynamically find the URL for viewing this models's details
        return reverse("art-detail", kwargs={'art_id': self.id})
    
    
class Copy(models.Model):
    art = models.ForeignKey(Art, on_delete=models.CASCADE)
    artist = models.CharField(max_length=100)
    date = models.DateField('Date Painted')
    notes = models.CharField(max_length=150)
    image = models.URLField(max_length=200)
    
    def __str__(self):
        return f"{self.artist} painted on {self.date}"
    
    class Meta:
        ordering = ['-date']
        # "-" newest dates with appear first
