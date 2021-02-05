from django.contrib import admin
from .models import Pay

@admin.register(Pay)
class PayAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'amount', 'paid')
    search_fields = ['name', 'email', 'guid']
