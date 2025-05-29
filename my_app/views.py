from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Art
from .forms import CopyForm
# from django.http import HttpResponse

# class Art:
#     def __init__(self, title, artist, date, medium, movement, image):
#         self.title = title
#         self.artist = artist
#         self.date = date
#         self.medium = medium
#         self.movement = movement
#         self.image = image

# art = [
#     Art('Sunrise', 'Claude Monet', 1872, "Oil", "Impression", "https://www.claude-monet.com/assets/img/paintings/impression-sunrise.jpg"),
#     Art('Sunrise', 'Claude Monet', 1872, "Oil", "Impression" , "https://www.claude-monet.com/assets/img/paintings/impression-sunrise.jpg"),
#     Art('Sunrise', 'Claude Monet', 1872, "Oil", "Impression", "https://www.claude-monet.com/assets/img/paintings/impression-sunrise.jpg"),
#     Art('Sunrise', 'Claude Monet', 1872, "Oil", "Impression", "https://www.claude-monet.com/assets/img/paintings/impression-sunrise.jpg")
# ]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def art_index(request):
    art = Art.objects.all()
    return render(request, 'art/index.html', {'art' : art})

def art_detail(request, art_id):
    art = Art.objects.get(id=art_id)
    copy_form = CopyForm()
    return render(request, 'art/detail.html', {
                'art' : art,
                'copy_form' : copy_form
                })


class ArtCreate(CreateView):
    model = Art
    fields = '__all__'
    
class ArtUpdate(UpdateView):
    model = Art
    fields = '__all__'

class ArtDelete(DeleteView):
    model = Art
    success_url = '/art/'