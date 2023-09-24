from django.shortcuts import render
from realty.models import Realty
import folium


def markers_views(request):
    realtys = Realty.objects.all()
    map_center = [49.80110956678017, 73.08109770179267]

    # city_map = folium.Map(location=map_center, zoom_start=14, control_scale=True, height='60%')

    city_map = folium.Map(location=map_center, zoom_start=14, control_scale=True, height='70%', control=True)

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

    return render(request, 'map.html', {'city_map': city_map._repr_html_()})
