from django.urls import path
from map.views import markers_views

urlpatterns = [
    path('', markers_views, name='map')
]