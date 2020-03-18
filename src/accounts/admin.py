from django.contrib import admin
from accounts.models import ZUser, University, MajorField, Field, EducationInfo, Country, State, City


# Register your models here.

@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    pass


@admin.register(MajorField)
class MajorFieldAdmin(admin.ModelAdmin):
    pass


@admin.register(Field)
class FieldAdmin(admin.ModelAdmin):
    pass


@admin.register(EducationInfo)
class EducationInfoAdmin(admin.ModelAdmin):
    pass


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    pass


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    pass


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    pass


@admin.register(ZUser)
class ZUserAdmin(admin.ModelAdmin):
    pass
