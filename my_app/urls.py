from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name="about"),
    path('accounts/signup/', views.signup, name="signup"),
    path('art/', views.art_index, name="art-index"),
    path('art/<int:art_id>/', views.art_detail, name="art-detail"),
    path('art/create/', views.ArtCreate.as_view(), name='art-create'),
    path('art/<int:pk>/update', views.ArtUpdate.as_view(), name='art-update'),
    path('art/<int:pk>/delete/', views.ArtDelete.as_view(), name="art-delete"),
    path('art/<int:art_id>/add-copy/', views.add_copy, name="add-copy"),
    path('list/create', views.ListCreate.as_view(), name='list-create'),
    path('list/<int:pk>/', views.ListDetail.as_view(), name='list-detail'),
    path('list/', views.ListList.as_view(), name='list-index'),
    path('list/<int:pk>/update', views.ListUpdate.as_view(), name='list-update'),
    path('list/<int:pk>/delete/', views.ListDelete.as_view(), name='list-delete'),
    path('art/<int:art_id>/associate-list/<int:list_id>/', views.associate_list, name='associate-list'),
    path('art/<int:art_id>/remove-list/<int:list_id>/', views.remove_list, name='remove-list'),
]
