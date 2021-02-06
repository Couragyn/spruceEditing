from django.contrib import admin
from .models import Pay
from django.utils.html import format_html
from django.conf import settings

@admin.register(Pay)
class PayAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'amount', 'paid')
    search_fields = ['name', 'email', 'guid']
    readonly_fields = ('url_field',)

    def url_field(self, obj):
        return '{}{}/{}'.format(settings.ROOT_URL, 'pay', obj.id)
