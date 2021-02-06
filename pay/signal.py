from django.shortcuts import get_object_or_404
from .models import Pay
from paypal.standard.ipn.signals import valid_ipn_received
from django.dispatch import receiver


@receiver(valid_ipn_received)
def payment_notification(sender, **kwargs):
    ipn = sender
    print(ipn)
    if ipn.payment_status == 'Completed':
        # payment was successful
        order = get_object_or_404(Pay, id=ipn.invoice)

        if order.amount() == ipn.mc_gross:
            # mark the order as paid
            order.paid = True
            order.save()
