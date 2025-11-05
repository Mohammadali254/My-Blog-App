from django.views.generic import ListView, DetailView
from .models import Post


# Create your views here.
class HomePageView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'

class PostDetailView(DetailView):
    model = Post
    template_name = 'blogapp/post_detail.html'
    context_object_name = 'post'
