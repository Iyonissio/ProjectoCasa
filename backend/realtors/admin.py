from django.contrib import admin
from .models import Realtor

class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'data_contratacao')
    list_per_page = 25

admin.site.register(Realtor, RealtorAdmin)
