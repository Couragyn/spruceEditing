from . import views
from django.urls import path
from django.conf.urls import url, include

urlpatterns = [
    path('pay/<uuid:id>/', views.process_payment, name='process_payment'),
    path('payment-done/', views.payment_done, name='payment_done'),
    path('payment-cancelled/', views.payment_canceled, name='payment_cancelled'),
    path('paypal/', include('paypal.standard.ipn.urls')),
]