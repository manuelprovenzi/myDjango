from django.contrib import admin
from .models import Telefono
from .models import Libro
from .models import Cd
from .models import City



# Register your models here.

admin.site.register(Telefono)
admin.site.register(Libro)
admin.site.register(Cd)
admin.site.register(City)
