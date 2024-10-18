from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView
from .models import Post

# def post_list(request):
#     posts = Post.objects.all()
#     return render(request,'post/list.html',{
#         'posts':posts
#     })

class PostList(ListView):
    model = Post
    
    context_object_name = 'posts'
    ordering  =  '-created_at'
    


class PostDetail(DetailView):
    model = Post


class PostCreate():
    pass

class PostDelete():
    pass
