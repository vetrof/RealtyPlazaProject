from django.db.models import Q, F
from django.shortcuts import render
from realty.models import Realty, TypeRealty
import folium
from django.template.loader import render_to_string


def markers_views(request):
    type_q = request.GET.get('types')
    min_s = request.GET.get('min_s')
    max_s = request.GET.get('max_s')
    min_p = request.GET.get('min_p')
    max_p = request.GET.get('max_p')
    text = request.GET.get('text')

    realtys = Realty.objects.all()
    types = TypeRealty.objects.all()

    if type_q:
        realtys = realtys.filter(type_realty=type_q)
    if min_s:
        realtys = realtys.filter(s__gte=min_s)
    if max_s:
        realtys = realtys.filter(s__lte=max_s)
    if min_p:
        realtys = realtys.filter(
            (Q(discount=0) & Q(price__gte=min_p)) |
            (Q(discount__gt=0) & Q(price__gte=(min_p + (F('price') * F('discount') / 100))))
        )
    if max_p:
        realtys = realtys.filter(
            (Q(discount=0) & Q(price__lte=max_p))
            (Q(discount__gt=0) & Q(price__lte=(max_p + (F('price') * F('discount') / 100))))
        )
    if text:
        realtys = realtys.filter(info__iregex=text)

    map_center = [49.80110956678017, 73.08109770179267]
    city_map = folium.Map(location=map_center, zoom_start=14, control_scale=True, height='100%', width='100%', scrollWheelZoom=False)

    for realty in realtys:
        popup_html = f'''
        <div style="width:200px">
            <strong>{realty.city}</strong><br>
            <strong>{realty.title}</strong><br>
            <strong>Комнаты:{realty.rooms}</strong><br>
            <strong>Стоимость:{realty.price}</strong><br>
            <strong><a href="{realty.get_absolute_url()}" target="_blank">Ссылка на объект</a></strong><br>

        </div>
        '''

        coordinates = (realty.latitude, realty.longitude)

        folium.Marker(
            coordinates,
            icon=folium.Icon(color='green'),
            tooltip=f'{realty.title}',
            popup=popup_html,).add_to(city_map)

    return render(request, 'map.html', {'city_map': city_map._repr_html_(), 'types': types})
