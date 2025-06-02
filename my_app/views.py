from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Art, List, Copy
from .forms import CopyForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

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
# def home(request):
#     return render(request, 'home.html')
class Home(LoginView):
    template_name = 'home.html'

def about(request):
    return render(request, 'about.html')

@login_required
def art_index(request):
    # art = Art.objects.all()
    art = Art.objects.filter(user=request.user)
    # art = request.user.art_set.all()
    return render(request, 'art/index.html', {'art' : art})

@login_required
def art_detail(request, art_id):
    art = Art.objects.get(id=art_id)
    # fetch all lists
    # lists = List.objects.all()
    # only get the lists the artwork has not been assigned to
    lists_art_is_not_on = List.objects.exclude(id__in = art.lists.all().values_list('id'))
    copy_form = CopyForm()
    return render(request, 'art/detail.html', {
                'art' : art,
                'copy_form' : copy_form,
                'lists' : lists_art_is_not_on,
                })

@login_required
def add_copy(request, art_id):
    # create a ModelForm instance using the data in request.POST
    form = CopyForm(request.POST)
    # validate the form
    if form.is_valid():
        # don't save the form to the db until it
        # has the art_id assigned
        new_copy = form.save(commit=False)
        new_copy.art_id = art_id
        new_copy.save()
    return redirect('art-detail', art_id = art_id)

@login_required
def associate_list(request, art_id, list_id):
    Art.objects.get(id=art_id).lists.add(list_id)
    return redirect('art-detail', art_id=art_id)

@login_required
def remove_list(request, art_id, list_id):
    Art.objects.get(id=art_id).lists.remove(list_id)
    return redirect('art-detail', art_id=art_id)

class ArtCreate(LoginRequiredMixin, CreateView):
    model = Art
    fields = ['title', 'artist', 'date', 'medium', 'movement', 'location', 'viewed', 'image']
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ArtUpdate(LoginRequiredMixin, UpdateView):
    model = Art
    fields = '__all__'

class ArtDelete(LoginRequiredMixin, DeleteView):
    model = Art
    success_url = '/art/'
    
class ListCreate(LoginRequiredMixin, CreateView):
    model = List
    fields = '__all__'
    
class ListList(LoginRequiredMixin, ListView):
    model = List
    
class ListDetail(LoginRequiredMixin, DetailView):
    model = List
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['arts'] = self.object.art_set.all()
        return context
        

class ListUpdate(LoginRequiredMixin, UpdateView):
    model = List
    fields = '__all__'
    
class ListDelete(LoginRequiredMixin, DeleteView):
    model = List
    success_url = '/list/'
    
    
def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('art-index')
        else:
            error_message = 'Invalid sign up - try again'
    # else - Get request, render signup.html
    form = UserCreationForm()
    return render(request, 'signup.html', {
        'form' : form,
        'error_message' : error_message,
    })