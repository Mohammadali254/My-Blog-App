from django.urls import path
from .views import (
    HomePageView,PostDetailView, CreatePostView, 
    PostUpdateView, PostDeleteView)

urlpatterns = [
    path('', HomePageView.as_view(), name = 'home'),
    path('post/<uuid:pk>/', PostDetailView.as_view(), name = 'post_detail'),
    path('create/', CreatePostView.as_view(), name = 'post_create'),
    path('post/<uuid:pk>/edit/', PostUpdateView.as_view(), name = 'post_edit'),
    path('post/<uuid:pk>/delete/', PostDeleteView.as_view(), name = 'post_delete'),
]