
from django.urls import path

from realty import views
from realty.views import detail_views, index_views, search_realty_views

# main_page/
urlpatterns = [
    path('', index_views, name='index_page'),
    path('realty/<int:id>/', detail_views, name='detail'),
    path('search/', search_realty_views, name='search_realty'),
    path('like/', views.like_views, name='like'),
    path('ranking/', views.realty_ranking_views, name='ranking'),

]

