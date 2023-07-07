from django.shortcuts import render

# Create your views here.
def lista_posts(request):
    posts = ['GPT-4', 'AutoGPT', 'AI Open Source']
    context = {
        'posts': posts
    }
    return render(request, 'posts.html', context)