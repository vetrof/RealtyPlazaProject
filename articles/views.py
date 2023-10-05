from django.http import HttpResponse
from django.shortcuts import render

from articles.models import Artile


def articles_view(request):
    articles = Artile
    return render(request, 'blog.html', {'articles': articles})
