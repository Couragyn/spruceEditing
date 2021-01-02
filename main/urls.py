from . import views
from django.urls import path
from .views import contact_page_view


urlpatterns = [
    path('contact/', contact_page_view.as_view(), name='contact')
]
