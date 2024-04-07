from django.shortcuts import render, redirect, get_object_or_404

from .models import Post
from .forms import PostForm  # Asigurați-vă că ați importat formularul


def post_list_view(request):
    # Obțineți toate postările din baza de date
    posts = Post.objects.all()

    # Verificați dacă cererea este de tip POST și tratați formularul, dacă este necesar
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            # Salvare postare doar dacă formularul este valid
            post = form.save()
            # Redirecționați către aceeași pagină pentru a evita re-trimiterea formularului
            return redirect('post_list')
    else:
        # Dacă cererea nu este de tip POST, creați un nou formular pentru a afișa
        form = PostForm()

    # Returnați șablonul HTML și transmiteți variabilele form și posts către șablon
    return render(request, 'post_list.html', {'form': form, 'posts': posts})

def post_detail_view(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'post_detail.html', {'post': post})
