from django.urls import path
from . import views

urlpatterns = [
    path('',views.getRoutes),
    path('posts/',views.getPosts),
    path('posts/<str:pk>/',views.getPost),
    path('users/',views.getUsers),
    path('users/<str:username>/',views.getUser),

    path('companies/',views.getCompanies),
]
