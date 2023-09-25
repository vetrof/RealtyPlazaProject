from django.contrib import admin

from users.models import Subscriber, Profile, Favorites


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'photo']
    raw_id_fields = ['user']



admin.site.register(Subscriber)
admin.site.register(Favorites)
