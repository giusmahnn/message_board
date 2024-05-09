from django.views.generic import ListView, TemplateView, DetailView
from .models  import Post
# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'

class PostPageView(ListView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'posts'

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'

class AboutPageView(TemplateView):
    template_name = 'about.html'
