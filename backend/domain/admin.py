from django.contrib import admin
from .models import DomainSearched,DomainEnding


# Register your models here.
class DomainSearchedAdminSettings(admin.ModelAdmin):
    filter_horizontal = ('searchers',)


admin.site.register(DomainEnding)
admin.site.register(DomainSearched,DomainSearchedAdminSettings)
