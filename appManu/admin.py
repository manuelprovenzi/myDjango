from django.contrib import admin
from .models import Telefono
from .models import Libro
from .models import Cd


# Register your models here.

admin.site.register(Telefono)
admin.site.register(Libro)
admin.site.register(Cd)