from django.contrib import admin
from .models import doctor,patient,appointment
# Register your models here.
admin.site.register(doctor)
admin.site.register(patient)
admin.site.register(appointment)

