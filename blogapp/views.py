from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import(
    ListView, DetailView,CreateView,UpdateView, DeleteView
)
from .models import Post
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from .forms import CommentForm


# Create your views here.
class HomePageView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'

class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'blogapp/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        context['comments'] = post.comments.all().order_by('-created_at')
        context['form'] = CommentForm()
        return context
    
    def post(self, request, *args, **kwargs):
        post = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_detail', pk = post.pk)
        
        context = self.get_context_data(form=form)
        return self.render_to_response(context)

class CreatePostView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blogapp/post_create.html'
    fields = ('title', 'body',)
    context_object_name = 'posts'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, "✅ Your post has been published successfully!")
        return super().form_valid(form)
    

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'blogapp/post_edit.html'
    fields = ('title', 'body',)
    success_url = reverse_lazy('home')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    
    def form_valid(self, form):
        messages.success(self.request, "✏️ Post updated successfully! ")
        return super().form_valid(form)
    
    
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blogapp/post_delete.html'
    success_url = reverse_lazy('home')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    
    