

from django.urls import path

from articles.views import articles_view


urlpatterns = [
    path('', articles_view, name='articles_page'),
    ]

