from django.urls import path
from realty.views import detail_views, index_views, search_realty_views
from tbot.views import telegram_page_views

# main_page/
urlpatterns = [
    path('', telegram_page_views, name='telegram_page'),

]

