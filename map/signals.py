from django.db.models.signals import post_save
from django.dispatch import receiver

from map.geocoding import address_to_coordinates
from realty.models import Realty


@receiver(post_save, sender=Realty)
def update_special_field(sender, instance, **kwargs):

    if instance.latitude == 0 and instance.longitude == 0:

        # Получаем значения field1 и field2
        city = instance.city
        street = instance.street
        house = instance.house



        coordinates = address_to_coordinates(city, street, house)

        # # # Устанавливаем результат в специальное поле
        if instance.latitude != coordinates[0] or instance.longitude != coordinates[1]:
            instance.latitude = coordinates[0]
            instance.longitude = coordinates[1]
            instance.save()