from django.contrib import admin
from .models import Pay
from django.utils.html import format_html
from django.conf import settings

@admin.register(Pay)
class PayAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'amount', 'paid', 'url_field','created_on')
    search_fields = ['name', 'email', 'guid']
    ordering = ('-created_on',)

    def url_field(self, obj):
        return '{}{}/{}'.format(settings.ROOT_URL, 'pay', obj.id)
