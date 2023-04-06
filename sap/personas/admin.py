from django.contrib import admin

# Register your models here.
from personas.models import Personas, Domicilio

admin.site.register(Personas)
admin.site.register(Domicilio)
