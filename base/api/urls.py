from django.urls import path
from . import views

urlpatterns = [
    path('',views.getRoutes),
    path('posts/',views.getPosts),
    path('posts/add/',views.addtPosts),
    path('posts/edit/<str:pk>/',views.editPost),
    path('posts/delete/<str:pk>/',views.deletePost),
    path('posts/<str:pk>/',views.getPost),

    path('users/',views.getUsers),
    path('users/recommended/',views.getRecommendedUsers),
    path('users/<str:username>/',views.getUser),

    path('companies/',views.getCompanies),
    path('company/<str:pk>/',views.getCompany),

    path('openings/',views.getLatestJobs),
]
