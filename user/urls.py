from django.urls import path
from user import views


urlpatterns = [
    path("", views.UserListView.as_view()),
    path('create', views.UserCreateView.as_view()),
    path('<int:pk>/update', views.UserUpdateView.as_view()),
    path("<int:pk>", views.UserDetailView.as_view()), 
    path("<int:pk>/delete", views.UserDeleteView.as_view()),
]