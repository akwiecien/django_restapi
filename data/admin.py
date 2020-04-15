from django.contrib import admin
from data.models import DataCity, DataCountry, DataContinent 


# Register your models here.
@admin.register(DataCity)
class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'type')
    list_editable = ('type',)

@admin.register(DataCountry)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('id', 'iso_code', 'name')

@admin.register(DataContinent)
class ContinentAdmin(admin.ModelAdmin):
    list_display = ('id', 'iso_code', 'name')