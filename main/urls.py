from . import views
from django.urls import path
from .views import contact_view, quote_view


urlpatterns = [
    path('contact/', contact_view.as_view(), name='contact'),
    path('quote/', quote_view.as_view(), name='quote'),
]
