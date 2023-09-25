

from django.urls import path
from ads import views



urlpatterns = [
    path("ad/", views.AdListView.as_view()),
    path('ad/create', views.AdCreateView.as_view()),
    path('ad/<int:pk>/update', views.AdUpdateView.as_view()),
    path("ad/<int:pk>", views.AdDetailView.as_view()), 
    path("ad/<int:pk>/upload_image", views.AdUploadImageView.as_view()),
    path("ad/<int:pk>", views.AdDeleteView.as_view()),
]