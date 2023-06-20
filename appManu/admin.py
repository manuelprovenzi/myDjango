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

def custom_titled_filter(title):
    class Wrapper(admin.FieldListFilter):
        def __new__(cls, *args, **kwargs):
            instance = admin.FieldListFilter.create(*args, **kwargs)
            instance.title = title
            return instance
    return Wrapper

class provinciaFilter(df.FilterSet):
    nomeProvincia = df.CharFilter(label='provincia')
    class Meta:
        model = City
        fields = ['nomeProvincia']
    

@admin.register(Libro)
class LibroAdmin(NumericFilterModelAdmin,admin.ModelAdmin):
    list_display = ("id", "autore", "titolo","genere","prezzo")
    list_filter = (
        ("id",custom_titled_filter("id")),
        ("autore",custom_titled_filter("autore")),
        ("titolo",custom_titled_filter("titolo")),
        ("prezzo",CustomSliderNumericFilter),
        ("prezzo",RangeNumericFilter),



    ) #("prezzo",SingleNumericFilter))#
    search_fields=("genere",)
    

#id autore titolo genere prezzo  data_pubblicazione descrizione

@admin.register(Telefono)
class TelefonoAdmin(admin.ModelAdmin):
    list_display = ("name", "schermo")
    list_filter = (
        ("schermo",custom_titled_filter("schermo")),
    )
    search_fields=("name",)

#name schermo

@admin.register(Cd)
class CdAdmin(admin.ModelAdmin):
    list_display = ("id", "titolo","artista","prezzo")
    list_filter = (
        ("id",custom_titled_filter("id")),
        ("artista",custom_titled_filter("artista")),
        ("anno",custom_titled_filter("anno")),

    )
    search_fields=("titolo",)
    #id titolo  artista nazione azienda prezzo anno

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display=("nomeCitta","nomeProvincia")
    list_filter = (
        ("nomeProvincia",custom_titled_filter("provincia")),
    )
    search_fields= ("nomeCitta",)
    #idCitta nomeCitta nomeProvincia


#mixin