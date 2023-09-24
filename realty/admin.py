from django.contrib import admin

from realty.models import Realty, City, Street, House, TypeRealty, Gallery


class RealtyAdmin(admin.ModelAdmin):
    list_display = ['id', 'type_realty', 'title', 'city']
    list_display_links = ('id', 'title')
    list_filter = ('type_realty', 'city', 'manager', 's', 'rooms', 'price', 'active')
    search_fields = ('type_realty', 'city')


admin.site.register(Realty, RealtyAdmin)
admin.site.register(City)
admin.site.register(Street)
admin.site.register(House)
admin.site.register(TypeRealty)
admin.site.register(Gallery)

