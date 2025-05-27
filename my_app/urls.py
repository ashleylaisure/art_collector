from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name="about"),
    path('art/', views.art_index, name="art-index"),
    path('art/<int:art_id>/', views.art_detail, name="art-detail"),
]
