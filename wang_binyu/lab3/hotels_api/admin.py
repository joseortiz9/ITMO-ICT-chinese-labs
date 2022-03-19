from django.contrib import admin

from hotels_api.models import Room, Hotel, Reservation

# Register your models here.
admin.site.register(Hotel)
admin.site.register(Room)
admin.site.register(Reservation)
