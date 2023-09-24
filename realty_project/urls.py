from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from manager.views import contacts_view
from tbot.views import telegram_webhook, my_test_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('map/', include('map.urls')),
    path('', include('realty.urls')),
    path('tbot/', telegram_webhook),
    path('telegram/', include('tbot.urls')),
    path('tbot/test/', my_test_view),
    path('contacts/', contacts_view, name='contacts'),
    path('users/', include('users.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



