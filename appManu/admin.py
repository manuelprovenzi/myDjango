from .models import Telefono
from .models import Libro
from .models import Cd
from .models import City
from django.contrib import admin
from admin_numeric_filter.admin import NumericFilterModelAdmin, SingleNumericFilter, RangeNumericFilter,SliderNumericFilter
import django_filters as df

class CustomSliderNumericFilter(SliderNumericFilter):
    MAX_DECIMALS = 2
    STEP = 10

class provinciaFilter(df.FilterSet):
    nomeProvincia = df.CharFilter(label='provincia')
    class Meta:
        model = City
        fields = ['nomeProvincia']
    
#
#@admin.register(YourModel)
#class YourModelAdmin(NumericFilterModelAdmin):
#    list_filter = (
#        ('field_A', SingleNumericFilter), # Single field search, __gte lookup
#        ('field_B', RangeNumericFilter), # Range search, __gte and __lte lookup
#        ('field_C', SliderNumericFilter), # Same as range above but with slider
#        ('field_D', CustomSliderNumericFilter), # Filter with custom attributes
#    )

# Register your models here.

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ("id", "autore", "titolo","genere","prezzo")
    list_filter = ("id", "autore","titolo",) #("prezzo",SingleNumericFilter))#
    search_fields=("genere",)
    

#id autore titolo genere prezzo  data_pubblicazione descrizione

@admin.register(Telefono)
class TelefonoAdmin(admin.ModelAdmin):
    list_display = ("name", "schermo")
    list_filter = ("schermo",)
    search_fields=("name",)

#name schermo

@admin.register(Cd)
class CdAdmin(admin.ModelAdmin):
    list_display = ("id", "titolo","artista","prezzo")
    list_filter = ("id","artista","anno")
    search_fields=("titolo",)
    #id titolo  artista nazione azienda prezzo anno

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display=("nomeCitta","nomeProvincia")
    list_filter = (("nomeProvincia"),)
    search_fields= ("nomeCitta",)
    #idCitta nomeCitta nomeProvincia


#mixin