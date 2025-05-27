from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('<h1>Your Art Collection</h1>')

def about(request):
    return HttpResponse('<h1>About your art collection</h1>')