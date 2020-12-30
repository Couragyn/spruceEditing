from . import views
from django.urls import path

urlpatterns = [
    path('contact/', views.contact_page, name='contact'),
    path('send-contact/', views.send_contact, name='send_contact')
]
