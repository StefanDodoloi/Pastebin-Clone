from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm

def post_list_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('post_list')
    posts = Post.objects.all()
    form = PostForm()
    return render(request, 'post_list.html', {'form': form, 'posts': posts})

def post_detail_view(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'post_detail.html', {'post': post})
