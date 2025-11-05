from django.urls import path
from .views import HomePageView,PostDetailView

urlpatterns = [
    path('', HomePageView.as_view(), name = 'home'),
    path('post/<uuid:pk>/', PostDetailView.as_view(), name = 'post_detail')
]