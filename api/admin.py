from django.contrib import admin
# Register your models here.
from api.models import Reservation, Festival

admin.site.register(Reservation)
admin.site.register(Festival)
