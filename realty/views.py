import folium
from django.db.models import CharField
from django.shortcuts import render

from map.map_operations import marker_and_maps
from realty.models import Realty
from users.models import Subscriber


def index_views(request):

    if request.method == 'POST':
        email = request.POST.get('email')
        Subscriber.objects.create(email=email)

    realtys = Realty.objects.all()
    city_map = marker_and_maps()

    return render(request, 'index.html', {'realtys': realtys, 'city_map': city_map._repr_html_()})


def detail_views(request, id):
    realty = Realty.objects.get(id=id)
    return render(request, 'detail.html', {'realty': realty, })


def search_realty_views(request):
    return render(request, 'search.html')
