from django.contrib import admin

from realty.models import Realty, City, Street, House, TypeRealty, Gallery, RubUsd

class GalleryInline(admin.TabularInline):
    fk_name = 'realty'
    model = Gallery


class RealtyAdmin(admin.ModelAdmin):
    list_display = ['id', 'type_realty', 'title', 'city']
    list_display_links = ('id', 'title')
    list_filter = ('type_realty', 'city', 'manager', 's', 'rooms', 'price', 'active')
    search_fields = ('type_realty', 'city')
    inlines = [GalleryInline,]


admin.site.register(Realty, RealtyAdmin)
admin.site.register(City)
admin.site.register(Street)
admin.site.register(House)
admin.site.register(TypeRealty)
admin.site.register(Gallery)

@admin.register(RubUsd)
class RubUsdAdmin(admin.ModelAdmin):
    list_display = ['rub_usd', 'usd_rub', 'date_get']

