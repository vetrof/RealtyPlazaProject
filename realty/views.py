import folium
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import CharField
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.db.models import Q, F, Value, IntegerField, ExpressionWrapper
from django.views.decorators.http import require_POST

from map.map_operations import marker_and_maps
from realty.models import Realty, TypeRealty
from users.models import Subscriber, Favorites


def index_views(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        Subscriber.objects.create(email=email)

    realtys = Realty.objects.all()
    city_map = marker_and_maps()

    return render(request, 'index.html', {'realtys': realtys, 'city_map': city_map._repr_html_()})


def detail_views(request, id):
    user = request.user

    # add to favorite
    if 'action' in request.GET and request.GET['action'] == 'add_to_favorites':
        realty_instance = Realty.objects.get(pk=id)
        user_instance = User.objects.get(username=user)
        Favorites.objects.get_or_create(realty=realty_instance, user=user_instance)
        return HttpResponseRedirect(request.path)

    is_favorite = Favorites.objects.filter(realty_id=id, user_id=user).exists()
    realty = Realty.objects.get(id=id)

    return render(request, 'detail.html', {'realty': realty, 'is_favorite': is_favorite})


def search_realty_views(request):
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
        search_words = text.split()
        q_objects = Q()
        for word in search_words:
            q_objects &= (Q(info__iregex=word) | Q(title__iregex=word))
        realtys = Realty.objects.filter(q_objects)

    return render(request, 'search.html', {'realtys': realtys, 'types': types})


@login_required
@require_POST
def like_views(request):
    print('**********')
    realty_id = request.POST.get('id')
    action = request.POST.get('action')

    if realty_id and action:
        try:
            realty = Realty.objects.get(id=realty_id)
            if action == 'like':
                realty.users_like.add(request.user)
            else:
                realty.users_like.remove(request.user)
            return JsonResponse({'status': 'ok'})

        except Realty.DoesNotExist:
            pass
    return JsonResponse({'status': 'error'})